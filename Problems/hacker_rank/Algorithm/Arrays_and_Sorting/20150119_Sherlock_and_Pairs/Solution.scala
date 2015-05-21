import scala.collection.mutable.HashMap

object Solution {
  def numOfPairs(ar: Array[Int]): BigInt = {
    val m: HashMap[Int, BigInt] = HashMap()
    for ( a <- ar )
      if ( m.contains(a - 1) )
        m.put(a - 1, m(a - 1) + 1)
      else
        m.put(a - 1, 1)
    m.filter(_._2 > 1).map((i: (Int, BigInt)) => i._2 * (i._2 - 1)).foldLeft(BigInt(0))(_ + _)
  }
  /*val MAX_CNT = 1000000
  def numOfPairs(ar: Array[Int]): Long = {
    var cnt: Long = 0
    var cnts = Array.fill[Int](MAX_CNT)(0)
    for ( i <- 0 until ar.length ) {
      cnts(ar(i) - 1) += 1
    }
    for ( i <- 0 until MAX_CNT ) {
      if ( 1 < cnts(i) ) {
        cnt += cnts(i).toLong * (cnts(i) - 1)
      }
    }
    cnt
  }*/
  def main(args: Array[String]) {
    val inps = io.Source.stdin.getLines.toArray
    val T = inps(0).toInt
    for ( i <- 2 to T * 2 by 2 )  {
      val ar = inps(i).split(" ").map((s: String) => s.toInt).toArray
      println(numOfPairs(ar))
    }
  }
}
