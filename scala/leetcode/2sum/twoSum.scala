//  https://leetcode.com/problems/two-sum

object Solution {
    //  runtime; 584ms, 30.25%
    //  memory; 60.4MB, 25.00%
    def twoSum(nums: Array[Int], target: Int): Array[Int] = {
       //val m = nums.groupBy(identity).mapValues(_.size)
       val m = nums.zipWithIndex.groupMap(_._1)(_._2)
       for ( n <- m.keys )  {
         val t = target - n
         val l = m.get(t)
         if ( l.isDefined ) {
           if ( t == n && 1 < l.get.size )
             return l.get.slice(0, 2).toArray
           else if ( t != n && 0 < l.get.size )
             return Array(m(n)(0), l.get(0))
         }
       }
       Array(-1, -1)
    }

    def main(args: Array[String]): Unit = {
      val data = List(Tuple3(Array(2, 7, 11, 15), 9, Array(0, 1)),
                      Tuple3(Array(3, 3), 6, Array(0, 1)),
                      Tuple3(Array(3, 2, 4), 6, Array(1, 2)),
                      Tuple3(Array(-3, 4, 3, 90), 0, Array(0, 2)))
      for ( t <- data ) {
        val (nums, target, expected) = t
        val real = twoSum(nums, target)
        println(s"(${nums.mkString(",")}) ${target} expected (${expected.mkString(",")}) real (${real.mkString(",")}) result ${expected(0) == real(0) && expected(1) == real(1)}")
      }
    }
}
