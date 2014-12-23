object Solution {
  def hasSubset(arr: Array[Int]): Boolean = {
    var i = 2
    val maxNum = arr.reduceLeft(_ max _)
    val noSet = Set(0)
    while ( i < maxNum + 1 )  {
      if ( arr.map(_ % i).toSet == noSet )  {
        return false
      }
      i += 1
    }
    true
  }
  def main(args: Array[String]) {
    val inps = io.Source.stdin.getLines.toArray.drop(1)
    for ( i <- 0 until inps.length by 2 ) {
      val arr = inps(i + 1).split(" ").map((s: String) => s.toInt)
      if ( hasSubset(arr) ) {
        println("YES")
      } else  {
        println("NO")
      }
    }
  }
}
