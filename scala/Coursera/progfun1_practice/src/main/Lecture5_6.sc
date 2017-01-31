/*
//  associativity
(xs ++ ys) ++ zs = xs ++ (ys ++ zs)
xs ++ Nil = xs
Nil ++ xs = xs
//  prove; structural induction
 */

/*
natural induction
to show a property P(n) for all the integers n >= b,
- show that we have P(b) (base case)
- for all integers n >= b show the induction step;
  if one has P(n), the one also has P(n + 1)
 */

def factorial(n: Int): Int =
  if ( n == 0 ) 1 //  1st clause
  else n * factorial(n - 1) //  2nd clause
/*
base case 4;
factorian(4) >= 2^4

induction step; n + 1
factorial(n + 1) >= (n + 1) * factorian(n)
                 > 2 * factorial(n)
                 >= 2 * power(2, n)
                 = power(2, n + 1)
                 = 2^(n + 1)
 */

//  referential transparency

//  structural induction
/*
P(xs) for all lists xs,
show that P(Nil) holds (base case),
for a list xs and some element x, show the induction step;
  if P(xs) holds, then P(x :: xs) also holds
 */
def concat[T](xs: List[T], ys: List[T]): List[T] = xs match {
  case List() => ys
  case x :: xs1 => x :: concat(xs1, ys)
}
/*
Base case; Nil
(Nil ++ ys) ++ zs = ys ++ zs
Nil ++ (ys ++ zs) = ys ++ zs

Induction step; x :: xs
((x :: xs) ++ ys) ++ zs = (x :: (xs ++ ys)) ++ zs
                        = x :: ((xs ++ ys) ++ zs)
                        = x :: (xs ++ (ys ++ zs))
(x :: xs) ++ (ys ++ zs) = x :: (xs ++ (ys ++ zs))
 */