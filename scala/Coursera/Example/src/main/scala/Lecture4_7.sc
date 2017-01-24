val fruit = List("apples", "oranges", "pears")
val diag3 = List(List(1, 0, 0), List(0, 1, 0), List(0, 0, 1))
//  like arrays, lists are homogeneous; the elements of a list must all have the same type

//  construction operation (pronounced cons)
"apples" :: ("oranges" :: ("pears" :: Nil))
1 :: (2 :: (3 :: (4 :: Nil)))
//  operators ending in ":" associate to the right
//  A :: B :: C is interpreted as A :: (B :: C)
//  the expression above is equivalent to
Nil.::(4).::(3).::(2).::(1)

fruit.head
fruit.tail
fruit.isEmpty

val empty = Nil
//empty.head

(1 :: (2 :: (List(3, 4) :: (5 :: Nil)))).length

def insert(x: Int, xs: List[Int]): List[Int] = xs match {
  case List() => List(x)
  case y :: ys => if ( x <= y ) x :: xs else y :: insert(x, ys)
}

def isort(xs: List[Int]): List[Int] = xs match {
  case List() => List()
  case y :: ys => insert(y, isort(ys))
}


