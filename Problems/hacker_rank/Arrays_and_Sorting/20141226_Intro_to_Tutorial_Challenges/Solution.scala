object Solution {
  def main(args: Array[String]) {
    val inps = io.Source.stdin.getLines.toArray
    val T = inps(0).toInt
    val n = inps(1).toInt
    val arr = inps(2).split(" ").map((s: String) => s.toInt)
    for ( i <- 0 until arr.length ) {
      if ( T == arr(i) )  {
        println(i)
        return
      }
    }
  }
}
