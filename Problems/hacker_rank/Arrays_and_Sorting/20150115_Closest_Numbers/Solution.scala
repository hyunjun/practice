object Solution {
  def main(args: Array[String]) {
    val inps = io.Source.stdin.getLines.toArray
    val ar = inps(1).split(" ").map((s: String) => s.toInt).toArray

    scala.util.Sorting.quickSort(ar)
    //for ( a <- ar ) println(a)
    //for ( a <- ar.slice(0, ar.length - 1).zip(ar.slice(1, ar.length)) ) println(a._1 + " " + a._2)
    //for ( m <- ar.slice(0, ar.length - 1).zip(ar.slice(1, ar.length)).map(a => a._2 - a._1) ) println(m)
    val pairs = ar.slice(0, ar.length - 1).zip(ar.slice(1, ar.length))
    val minDiff = pairs.map(a => a._2 - a._1).reduceLeft(_ min _)
    //for ( a <- ar.slice(0, ar.length - 1).zip(ar.slice(1, ar.length)).filter(a => a._2 - a._1 == minDiff) )
    //  println(a._1 + " " + a._2)
    println(pairs.filter(a => a._2 - a._1 == minDiff).map(a => a._1 + " " + a._2).mkString(" "))
  }
}
