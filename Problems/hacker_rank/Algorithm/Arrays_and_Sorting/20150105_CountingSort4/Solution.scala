object Solution {
  /*def countingSort(ar: Array[(Int, String)]): String = {
    val counts: Array[Array[String]] = Array.fill[Array[String]](100)(Array())
    for ( (x, s) <- ar ) {
      counts(x) = counts(x) :+ s
    }
    (for { c <- counts if ( 0 < c.length ) } yield c.mkString(" ")).mkString(" ")
  }
  def main(args: Array[String]) {
    val inps = io.Source.stdin.getLines.toArray
    val n = inps(0).toInt
    var ar: Array[(Int, String)] = Array()
    for ( i <- 1 to n )  {
      if ( i <= n / 2 )  {
        ar = ar :+ (inps(i).split(" ")(0).toInt, "-")
      } else  {
        ar = ar :+ (inps(i).split(" ")(0).toInt, inps(i).split(" ")(1))
      }
    }
    println(countingSort(ar))
  }*/
  /*def countingSort(ar: Array[(Int, String)]): String = {
    val counts: Map[Int, Array[String]] = Map()
    for ( (x, s) <- ar ) {
      counts(x) = counts(x) :+ s
    }
    (for { c <- counts if ( 0 < c.length ) } yield c.mkString(" ")).mkString(" ")
  }
  def main(args: Array[String]) {
    /*val inps = io.Source.stdin.getLines.toArray
    val n = inps(0).toInt
    val ar = (for ( i <- 1 to n )
                  yield (inps(i).split(" ")(0).toInt,
                        if ( i <= n / 2) "-" else inps(i).split(" ")(1))).toArray
    println(countingSort(ar))
  }*/
  def countingSort(ar: IndexedSeq[(Int, String)]): String = {
    val res = for ( i <- 0 until 100 )
      yield ar.filter((t: (Int, String)) => t._1 == i).map((t: (Int, String)) => t._2).mkString(" ")
    res.mkString(" ")
  }

  def main(args: Array[String]) {
    val inps = io.Source.stdin.getLines.toArray
    val n = inps(0).toInt
    val ar = for ( i <- 1 to n )
                  yield (inps(i).split(" ")(0).toInt,
                        if ( i <= n / 2) "-" else inps(i).split(" ")(1))
    println(countingSort(ar))
  }
}
