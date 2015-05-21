object Solution {
  def main(args: Array[String]) {
    val inps = io.Source.stdin.getLines.toArray
    val ar = inps(1).split(" ").map((s: String) => s.toInt).toArray

    scala.util.Sorting.quickSort(ar)
    println(ar(ar.length / 2))
  }
}
