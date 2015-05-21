object Solution {
  def main(args: Array[String]) {
    val inps = io.Source.stdin.getLines.toArray
    val t = inps(0).toInt
    for ( i <- 1 to t ) {
      val ar = inps(i).split(" ").map((s: String) => s.toInt).toArray
      val r = ar(0)
      val k = ar(1)
      val radius = Math.sqrt(r)
      val end = if ( radius - radius.toInt == 0 ) radius.toInt else radius.toInt + 1
      val cnt = 4 * (0 until end).map((x: Int) => Math.sqrt(r - x * x)).filter((y: Double) => y - y.toInt == 0).size
      if ( cnt <= k )
        println("possible")
      else
        println("impossible")
    }
  }
}
