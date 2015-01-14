object Solution {
  def mergeSort(arr: Array[Int]): (Array[Int], Int) = {
    val l = arr.length
    if (l < 2)
      return (arr, 0)
    val m = l / 2
    var (left, lCnt) = mergeSort(arr.slice(0, m))
    var (right, rCnt) = mergeSort(arr.slice(m, l))
    var cnt = lCnt + rCnt
    var res: Array[Int] = Array()
    println("left\t" + left.mkString(" ") + "\tright\t" + right.mkString(" "))
    var (idx, lIdx, rIdx) = (0, 0, 0)
    while ( 0 < left.length && 0 < right.length ) {
      if ( left(0) <= right(0) )  {
        res(idx) = left(0)
        //res = res :+ left(0)
        left = left.drop(1)
      } else  {
        cnt += left.length
        res(idx) = right(0)
        //res = res :+ right(0)
        right = right.drop(1)
      }
      idx += 1
    }
    res = res.dropRight(res.length - idx)
    println(res.mkString(" ") + "\t[" + cnt + "]")
    (res ++ left ++ right, cnt)
  }
  def mergeSort2(arr: Array[Int]): (Array[Int], BigInt) = {
    val l = arr.length
    if (l < 2)
      return (arr, 0)
    val m = l / 2
    var (left, lCnt) = mergeSort2(arr.slice(0, m))
    var (right, rCnt) = mergeSort2(arr.slice(m, l))
    var cnt: BigInt = lCnt + rCnt
    var res: Array[Int] = Array.fill[Int](left.length + right.length)(0)
    var (idx, lIdx, rIdx) = (0, 0, 0)
    while ( lIdx < left.length && rIdx < right.length ) {
      if ( left(lIdx) <= right(rIdx) ) {
        res(idx) = left(lIdx)
        lIdx += 1
      } else  {
        cnt += left.length - lIdx
        res(idx) = right(rIdx)
        rIdx += 1
      }
      idx += 1
    }
    while ( lIdx < left.length )  {
      res(idx) = left(lIdx)
      idx += 1
      lIdx += 1
    }
    while ( rIdx < right.length )  {
      res(idx) = right(rIdx)
      idx += 1
      rIdx += 1
    }
    (res, cnt)
  }

  def main(args: Array[String]) {
    val inps = io.Source.stdin.getLines.toArray
    for ( i <- Range(1, inps(0).toInt * 2, 2) )  {
      val n = inps(i).toInt
      val arr = inps(i + 1).split(" ").map((s: String) => s.toInt).toArray
      println(mergeSort2(arr)._2)
    }
  }
}
