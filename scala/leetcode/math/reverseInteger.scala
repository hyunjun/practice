//  https://leetcode.com/problems/reverse-integer

object Solution {
  //  runtime; 444ms, 13.28%
  //  memory; 54.2MB, 100.00%
  def reverse(x: Int): Int = {
    val limit = math.pow(2, 31).toInt
    if ( x < -limit || limit - 1 < x )
      return 0
    val s = x.toString
    try {
      s(0) match {
        case '-' => -1 * s.slice(1, s.length).reverse.toInt
        case _ => s.reverse.toInt
      }
    } catch {
      case e: NumberFormatException => 0
    }
  }

  def main(args: Array[String]): Unit = {
    val data = List(Tuple2(123, 321),
                    Tuple2(-123, -321),
                    Tuple2(120, 21),
                    Tuple2(-120, -21),
                    Tuple2(0, 0),
                    Tuple2(1534236469, 0))
    for ( t <- data ) {
      val (x, expected) = t
      val real = reverse(x)
      println(s"${x} expected ${expected} real ${real} result ${expected == real}")
    }
  }
}
