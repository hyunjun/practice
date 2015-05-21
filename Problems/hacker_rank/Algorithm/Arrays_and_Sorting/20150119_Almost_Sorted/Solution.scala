object Solution {
  def isPossibleToSort(ar: Array[Int])  {
    var l = 0
    var r = ar.length - 1
    while ( l < r && ar(l) < ar(l + 1) )  l += 1
    while ( 0 < r && ar(r - 1) < ar(r) )  r -= 1

    val sorted: Array[Int] = ar.sorted
    if ( sorted.sameElements(((ar.slice(0, l) :+ ar(r)) ++ ar.slice(l + 1, r) :+ ar(l)) ++ ar.slice(r + 1, ar.length)) )
      println(s"yes\nswap ${l + 1} ${r + 1}")
    else if ( sorted.sameElements(ar.slice(0, l) ++ ar.slice(l, r + 1).reverse ++ ar.slice(r + 1, ar.length)) ) 
      println(s"yes\nreverse ${l + 1} ${r + 1}")
    else
      println("no")
  }
  def main(args: Array[String]) {
    val inps = io.Source.stdin.getLines.drop(1).toArray
    val ar = inps(0).split(" ").map((s: String) => s.toInt).toArray
    isPossibleToSort(ar)
  }
}
