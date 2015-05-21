object Solution {
  def insertionSort(arr: Array[Int])  {
    var V = arr(arr.length - 1)
    var idx = arr.length - 2
    while ( -1 < idx && V < arr(idx) )  {
      arr(idx + 1) = arr(idx)
      println(arr.mkString(" "))
      idx -= 1
    }
    arr(idx + 1) = V
    println(arr.mkString(" "))
  }
  def main(args: Array[String]) {
    val inps = io.Source.stdin.getLines.drop(1).toArray
    val arr = inps(0).split(" ").map((s: String) => s.toInt).toArray
    insertionSort(arr)
  }
}
