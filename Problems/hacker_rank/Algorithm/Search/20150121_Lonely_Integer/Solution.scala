import scala.collection.mutable.HashMap

object Solution {
  def main(args: Array[String]) {
    val inps = io.Source.stdin.getLines.drop(1).toArray
    val ar = inps(0).split(" ").map((s: String) => s.toInt).toArray
    val m: HashMap[Int, Int] = HashMap()
    for ( a <- ar ) {
      if ( m.contains(a) )
        m.put(a, m(a) + 1)
      else
        m.put(a, 1)
    }
    println(m.retain((k, v) => v == 1).keys.head)
  }
}
