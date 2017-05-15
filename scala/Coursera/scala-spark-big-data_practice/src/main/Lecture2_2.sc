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