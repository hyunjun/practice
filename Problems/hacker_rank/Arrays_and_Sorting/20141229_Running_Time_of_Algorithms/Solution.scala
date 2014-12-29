object Solution {
  def insertionSort(arr: Array[Int]): Int = {
    var cnt: Int = 0
    for ( i <- 1 until arr.length ) {
      for ( j <- i until 0 by -1 )  {
        if ( arr(j) < arr(j - 1) )  {
          //  http://stackoverflow.com/questions/10158405/swapping-array-values-with-for-and-yield-scala
          val tmp = arr(j)
          arr(j) = arr(j - 1)
          arr(j - 1) = tmp
          cnt += 1
        }
      }
    }
    cnt
  }

  def main(args: Array[String]) {
    val inps = io.Source.stdin.getLines.drop(1).toArray
    val arr = inps(0).split(" ").map((s: String) => s.toInt).toArray
    println(insertionSort(arr))
  }
}
