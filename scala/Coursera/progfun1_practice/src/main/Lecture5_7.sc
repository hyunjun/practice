/*
      Nil.reverse = Nil
(x :: xs).reverse = xs.reverse ++ List(x)
 */
Nil.reverse.reverse == Nil.reverse
Nil.reverse == Nil
/*
(x :: xs).reverse.reverse
= (xs.reverse ++ List(x)).reverse
*/

/*
(xs.reverse ++ List(x)).reverse = x :: xs.reverse.reverse
//  generalize
(ys ++ List(x)).reverse = x :: ys.reverse

ys = Nil
(Nil ++ List(x)).reverse = List(x).reverse
                         = (x :: Nil).reverse
                         = Nil.reverse ++ List(x)
                         = Nil ++ (x :: Nil)
                         = x :: Nil
                         = x :: Nil.reverse

((y :: ys) ++ List(x)).reverse = (y :: (ys ++ List(x))).reverse //  unfold
                               = (ys ++ List(x)).reverse ++ List(y)
                               = (x :: ys.reverse) ++ List(y)
                               = x :: (ys.reverse ++ List(y))
                               = x :: (y :: ys).reverse //  fold
 */

/*
(xs ++ ys) map f = (xs map f) ++ (ys map f)

//  clauses
      Nil map f = Nil
(x :: xs) map f = f(x) :: (xs map f)
 */