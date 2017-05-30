//----------------------------------------------
//  Shuffling: What it is and why it's important
//----------------------------------------------
case class CFFPurchase(customerId: Int, destination: String, price: Double)
/*
val purchasesRdd: RDD[CFFPurchase] = sc.textFile(...)
val purchasesPerMonth =
  purchasesRdd.map(p => (p.customerId, p.price))  //  Pair RDD
              .groupByKey() //  returns RDD[K, Iterable[V]]
              .map(p => (p._1, (p._2.size, p._2.sum))
              .collect()
*/
val purchases = List(CFFPurchase(100, "Geneva", 22.25),
                     CFFPurchase(100, "Lucerne", 31.60),
                     CFFPurchase(100, "Fribourg", 12.40),
                     CFFPurchase(200, "St. Gallen", 8.20),
                     CFFPurchase(300, "Zurich", 42.10),
                     CFFPurchase(300, "Basel", 16.20))
/*
//  result of shuffle, groupByKey()
(100, [22.25, 12.40, 31.60])
(200, [8.20])
(300, [42.10, 16.20])

//  however, distribute by network; too slow

def reduceByKey(func: (V, V) => V): RDD[(K, V)]

val purchasesPerMonth =
  purchasesRdd.map(p => (p.customerId, (1, p.price)))  //  Pair RDD
              .reduceByKey((v1, v2) => (v1._1 + v2._1, v1._2 + v2._2))
              .collect()
//  after map
(100, (2, 53.85))

(100, (1, 12.40))
(200, (1, 8.20))

(300, (2, 58.30))

//  after reduceByKey, result will be the same as above
//  however, the amount of data over network reduced
//           by using groupByKey + map -> reduceByKey
 */


//--------------
//  Partitioning
//--------------

//  Hash & Range partitioning
//  Customizing a partitioning is only possible on Pair RDDs
/*
val purchasesPerCust =
  purcasesRdd.map(p => (p.customerId, p.price)) //  pair RDD
             .groupByKey()
  p = k.hashCode() % numPartitions
*/

//  range partitioning
//    1. an ordering for keys
//    2. a set of sorted ranges of keys
//    tuples with keys in the same range appear on the same machine

//  a pair RDD, with keys [8, 96, 240, 400, 401, 800]
//    and a desired number of partitions of 4
//    suppose, hashCode is the identity (n.hashCode() == n)
/*
p = k.hashCode() % numPartitions = k % 4
partition 0: [8, 96, 240, 400, 800]
partition 1: [401]
partition 2: []
partition 3: []
//  unbalanced and hurts performance
*/
/*
//  set of ranges: [1, 200], [201, 400], [401, 600], [601, 800]
//    if key is non negative and 800 is the biggest
partition 0: [8, 96]
partition 1: [240, 400]
partition 2: [401]
partition 3: [800]
*/


//  1. partitionBy on an RDD, providing an explicit Partitioner
//  2. using transformations that return RDDs with specific partitioners

//  partitionBy
/*
val pairs = purchasesRdd.map(p => (p.customerId, p.price))

val tunedPartitioner = new RangePartitioner(8, pairs)
val partitioned = pairs.partitionBy(tunedPartitioner)
                       .persist() //  once moved, keep it in memory
*/
//  1. specifiying the desired number of partitions
//  2. providing a pair RDD with ordered keys

//  partitioner from parent RDD; configured to use hash partitioner
//  automatically-set partitioner; sortByKey, a RangePartitioner is used

/*
cogroup
groupWith
join
leftOuterJoin
rightOuterJoin
groupByKey
reduceByKey
foldByKey
combineByKey
partitionBy
sort
mapValues (if parent has a partitioner)
flatMapValues (if parent has a partitioner)
filter (if parent has a partitioner)
//  all other operations will produce a result without a partitioner
//    why?
//    consider the map transformation
//    because it's possible for map to change the key
//    rdd.map((k: String, v: Int) => ("doh!", v))
//    although parent RDD ahs partitioner, map result RDD makes sense because key has changed
 */


//------------------------------
//  Optimizing with Partitioners
//------------------------------
/*
val purchasesPerCust = partitioned.map(p => (p._1, (1, p._2)))
val purchasesPerMonth = purchasesPerCust.reduceByKey((v1, v2) => (v1._1 + v2._1, v1._2 + v2._2))
                                        .collect()
//  reduceByKey 9x times faster than map + groupByKey
*/

/*
//  Learning Spark book, pp61-64
val sc = new SparkContext(...)
val userData = sc.sequenceFile[UserID, userInfo]("hdfs://...").persist()

def processNewLogs(logFileName: String): Unit = {
  val events = sc.sequenceFile[UserID, LinkInfo](logFileName)
  val joined = userData.join(events)  //  RDD of (UserID, (UserInfo, LinkInfo))
  val offTopicVisits = joined.filter {
    case (userId, (userInfo, linkInfo)) =>  //  Expand the tuple
      !userInfo.topics.contains(linkInfo.topic)
  }.count()
  println("Number of visits to non-subscribed topics: " + offTopicVisits)
}
//  It will be inefficient!
//  each time processNewLogs invoked, does not know how the keys are partitioned in the datasets

//  userData becomes
val userData = sc.sequenceFile[UserID, UserInfo]("hdfs://...")
                 .partitionBy(new HashPartitioner(100))
                 .persist()
//  userData.join(events), Spark will shuffle only the events RDD
*/

/*
val purchasesPerCust = purchasesRdd.map(p => (p.customerId, p.price))
                                   .groupByKey()
//  Rule of Thumb; a shuffle can occur when the resulting RDD depends on
//                 other elements from the same or another RDD
*/

//  Operations that might cause a shuffle
/*
cogroup, groupWith
join, leftOuterJoin, rightOuterJoin
groupByKey, reduceByKey, combineByKey
distinct, intersection, repartition, coalesce
 */


//-----------------------------
//  Wide vs Narrow Dependencies
//-----------------------------
//  Lineages
//  Computations on RDDs are represented as a lineage graph; a Directed Acyclic Graph

//  RDDs are made up of 2 important parts(totally in 4 parts)
//    Partitions. Atomic pieces of the dataset.
//                One or many per computation node
//    Dependencies. Models relationship between this RDD and its partitions
//                  with the RDD(s) it was derived from
//    A function for computing the dataset based on its parent RDDs
//    Metadata about its partitioning scheme and data placement

//  Transformations cause shuffle
//  Narrow dependencies; Each partition of the parent RDD
//                       is used by at most one partition of the child RDD
//                       Fase, no shuffle necessary. Optimizations like piepelining possible
//                       e.g. map, mapValues, flatMap, filter, union
//                            mapPartitions, mapPartitionsWithIndex
//                            join with co-partitioned inputs
//                       OneToOneDependency, PruneDependency, RangeDependency
//  Wide dependencies; Each partition of the parent RDD
//                     may be depended on by multiple child partitions
//                     Slow, requires all or some data to be shuffled over the network
//                     e.g. groupByKey. join with inputs not co-partitioned
//                          cogroup, groupWith, join, leftOuterJoin, rightOuterJoin
//                          groupByKey, reduceByKey, combineByKey
//                          distinct, intersection, repartition, coalesce
//                     ShuffleDependency
/*
val wordsRdd = sc.parallelize(largeList)
val pairs = wordsRdd.map(c => (c, 1))
                    .groupByKey()
                    .toDebugString
//  toDebugString visualizes RDD's lineage
 */


//  Lineage graphs are the key to fault tolerence in Spark