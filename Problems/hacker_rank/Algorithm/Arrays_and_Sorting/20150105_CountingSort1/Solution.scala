object Solution {
  def countingSort(ar: Array[Int]): Array[Int] = {
    val res: Array[Int] = Array.fill[Int](100)(0)
    for ( a <- ar ) {
      res(a) += 1
    }
    res
  }

  def main(args: Array[String]) {
    val inps = io.Source.stdin.getLines.drop(1).toArray
    val ar = inps(0).split(" ").map((s: String) => s.toInt).toArray
    val res = countingSort(ar)
    println(res.mkString(" "))
  }
}
