object Solution {
  def decentNumber(n: Int): String = {
    val fiveStart: Int = Range(n, -1, -1).filter((i: Int) => i % 3 == 0)(0)
    val threeStart: Int = Range(n, -1, -1).filter((i: Int) => i % 5 == 0)(0)
    for ( f <- fiveStart to 0 by -3;
          t <- threeStart to 0 by -5 ) {
      if ( f + t == n )
        return "5" * f + "3" * t
    }
    "-1"
  }
  def main(args: Array[String]) {
    val inps = io.Source.stdin.getLines.drop(1).map((s: String) => s.toInt)
    for ( i <- inps ) {
      println(decentNumber(i))
    }
  }
}
