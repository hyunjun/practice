"Hello World"
val fruitList = List("apples", "oranges", "pears")
val fruit = "apples" :: ("oranges" :: ("pears" :: Nil))
fruit.head
fruit.tail
val empty = List()
val empty2 = Nil

val nums = Vector("louis", "frank", "hiromi")
nums(1)
nums.updated(2, "helena")

val fruitSet = Set("apple", "banana", "pear", "banana")
fruitSet.size

val r: Range = 1 until 5
val s: Range = 1 to 5
1 to 10 by 3
6 to 1 by -2

val s2 = (1 to 6).toSet
s2 map (_ + 2)

val s3 = "Hello World"
s3 filter (c => c.isUpper)

val xs = Stream(1, 2, 3)
val xs2 = Stream.cons(1, Stream.cons(2, Stream.cons(3, Stream.empty)))
(1 to 1000).toStream
val x = 30000
x #:: xs

val pair = ("answer", 42)
val (label, value) = pair
pair._1 == label
pair._2

val M = 2
val N = 3
for (x <- 1 to M; y <- 1 to N)
  yield(x, y)
(1 to M) flatMap (x => (1 to N) map (y => (x, y)))

/*
for {
  i <- 1 until n
  j <- 1 until if
  if isPrime(i + j)
} yield (i, j)
*/