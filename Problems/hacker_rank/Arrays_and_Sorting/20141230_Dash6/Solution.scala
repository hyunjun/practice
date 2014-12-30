object Solution {
  def partition(ar: Array[Int]): Array[Int] = {
    (ar.filter(_ < ar(0)) :+ ar(0)) ++ ar.filter(ar(0) < _)
  }

  def main(args: Array[String]) {
    val inps = io.Source.stdin.getLines.drop(1).toArray
    val ar = inps(0).split(" ").map((s: String) => s.toInt).toArray
    val res = partition(ar)
    println(res.mkString(" "))
  }
}
