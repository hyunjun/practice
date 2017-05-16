//**********************
//  Reduction Operations
//  https://www.coursera.org/learn/scala-spark-big-data/lecture/GssIT/reduction-operations
//**********************

case class Taco(kind: String, price: Double)

val tacoOrder =
  List(
    Taco("Carnitas", 2.25),
    Taco("Corn", 1.75),
    Taco("Barbacoa", 2.50),
    Taco("Chicken", 2.00)
  )
val cost = tacoOrder.foldLeft(0.0)((sum, taco) => sum + taco.price)

//  foldLeft; not parallelizabl

val xs = List(1, 2, 3, 4)
val res = xs.foldLeft("")((str: String, i: Int) => str + i)
//  List(1, 2) / List(3, 4)
//  String "12" / String "34"
//  type error because foldLeft above needs (String, Int) type

//  Parallel Reduction Operations; Fold
//  def fold(z: A)(f: (A, A) => A): A

//  aggregate[B](z: => B)(seqop: (B, A) => B, comboop: (B, B) => B): B
//  parallelizable
//  possible to change the return type

//  Scala     vs. Spark
//  fold      vs. fold
//  foldLeft/foldRight  vs. X
//  reduce    vs. reduce
//  aggregate vs. aggregate

//***********
//  Pair RDDs
//  https://www.coursera.org/learn/scala-spark-big-data/lecture/d5gwX/pair-rdds
//***********

//  distributed key value pairs = Pair RDDs, RDD[(K, V)]

//  val rdd: RDD[WikipediaPage] = ...
//  val pairRdd = rdd.map(page = > (page.title, page.text))
//  now can use reduceByKey, groupByKey, join...

//******************************************
//  Trnasformations and Actions on Pair RDDs
//  https://www.coursera.org/learn/scala-spark-big-data/lecture/YV3BH/transformations-and-actions-on-pair-rdds
//******************************************
//  Trnasformations
//    groupByKey
//    reduceByKey
//    mapValues
//    keys
//    join
//    leftOuterJoin / rightOuterJoin
//  Action
//    countByKey

//  Recal groupBy from Scala collections
//    def groupBy[K](f: A => K): Map[K, Traversable[A]]
val ages = List(2, 52, 44, 23, 17, 14, 12, 82, 51, 64)
val grouped = ages.groupBy { age =>
  if ( age >= 18 && age < 65 ) "adult"
  else if ( age < 18 ) "child"
  else "senior"
}

//  def groupByKey(): RDD[(K, Iterable[V])]
//  case class Event(organizer: String, name: String, budget: Int)
//  val eventsRdd = sc.parallelize(...).map(event => (event.organizer, event.budget))
//  val groupedRdd = eventsRdd.groupByKey()
//  groupedRdd.collect().foreach(println)
//  (Prime Sound, CompactBuffer(42000))
//  (Sportorg, CompactBuffer(23000, 12000, 1400))

//  def reduceByKey(func: (V, V) => V): RDD[(K, V)]
//    = groupByKey + reduce, more efficient than using each separately
//  val budgetsRdd = eventsRdd.reduceByKey(_+_)
//  budgetsRdd.collect().foreach(println)
//  (Prime Sound, 42000)
//  (Sportorg, 36400)

//  def mapValues[U](f: V => U): RDD[(K, U)]
//    shorthand for rdd.map { case (x, y): (x, func(y)) }

//  def countByKey(): Map[K, Long]

//  val intermediate =
//    eventsRdd.mapValues(b => (b, 1))
//             // (organizer K, budget V) -> (organizer, (budget, 1))
//             .reduceByKey((v1, v2) => (v1._1 + v2._1, v1._2 + v2._2)
//             // (organizer, (total budget, total # of budgets))
//  val avgBudgets =
//    intermediate.mapValues {
//      case (budget, numberOfEvents) => budget / numberOfEvents
//    }
//  avgBudgets.collect().foreach(println)
//  (Prime Sound, 42000)
//  (Sportorg, 12133)

//  def keys: RDD[K]
//  case class Visitor(ip: String, timestamp: String, duration: String)
//  val visits: RDD[Visitor] = sc.textFile(...).map(v => (v.ip, v.duration))
//  val numUniqueVisits = visits.keys.distinct().count()
