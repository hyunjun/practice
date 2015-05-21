object Solution {
  def countingSort(ar: Array[Int]): Array[Int] = {
    val counts: Array[Int] = Array.fill[Int](100)(0)
    for ( a <- ar ) {
      counts(a) += 1
    }
    for ( i <- 1 until 100 )  {
      if ( 0 < counts(i) )  {
        counts(i) += counts(i - 1)
      } else if ( 0 == counts(i) )  {
        counts(i) = counts(i - 1)
      }
    }
    counts
  }

  def main(args: Array[String]) {
    val inps = io.Source.stdin.getLines.drop(1).toArray
    val ar = inps.map((s: String) => s.split(" ")(0).toInt).toArray
    val res = countingSort(ar)
    println(res.mkString(" "))
  }
}
