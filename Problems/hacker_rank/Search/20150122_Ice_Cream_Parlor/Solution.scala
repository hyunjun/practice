object Solution {
  def main(args: Array[String]) {
    val inps = io.Source.stdin.getLines.toArray
    val t = inps(0).toInt
    for ( i <- 1 to t * 3 by 3 )  {
      val m = inps(i).toInt
      val n = inps(i + 1).toInt
      val flavors = inps(i + 2).split(" ").map((s: String) => s.toInt).toArray
      /*for ( a <- 0 until flavors.length - 1 ) {
        for ( b <- a + 1 until flavors.length ) {
          if ( flavors(a) + flavors(b) == m ) {
            println(s"${a + 1} ${b + 1}")
          }
        }
      }*/
      /*for ( a <- 0 until flavors.length - 1;
            b <- a + 1 until flavors.length;
            if flavors(a) + flavors(b) == m )
        println(s"${a + 1} ${b + 1}")*/
      (0 until flavors.length - 1).flatMap(a => (a + 1 until flavors.length).filter(flavors(a) + flavors(_) == m).map((a, _))).foreach(r => println(s"${r._1 + 1} ${r._2 + 1}"))
    }
  }
}
