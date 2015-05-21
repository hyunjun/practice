object Solution {
  def main(args: Array[String]) {
    val inps = io.Source.stdin.getLines.toArray
    val in = inps(0).split(" ").map((s: String) => s.toInt)
    val ar = inps(1).split(" ").map((s: String) => s.toInt)
    val idx = ar.length - in(1) % in(0)
    val rotated = ar.slice(idx, ar.length) ++ ar.slice(0, idx)
    for ( i <- Range(2, 2 + in(2)) )  {
      println(rotated(inps(i).toInt))
    }
  }
}
