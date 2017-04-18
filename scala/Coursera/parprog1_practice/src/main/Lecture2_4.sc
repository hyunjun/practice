//  Using sum. array of norm
//  reduce(map(a, power(abs(_), p)), _ + _)
List(1, 3, 8).map(t => t * t).reduce(_ + _)


/*  associative but not commutative
    reduce still gives the same result because they are associative
 */
//  concatenation (append) of lists
//  concatenation of Strings
//  matrix multiplication AB
//  composition of relations
//  composition of functions

/*  Many operations are commutative but not associative
    f(x, y) = x * x + y * y

    f(x, y) == f(y, x)
    f(f(x, y), z) != f(x, f(y, z))
 */

//  associativity is not preserved by mapping

val e = 1e-200
val x = 1e200
val mx = -x

//  floating point addition is commutative but not associative
val a = (x + mx) + e
val b = x + (mx + e)  //  mx + e is not calculated precisely
a == b

//  floating point multiplication is commutative but not associative
val c = (e * x) * x
val d = e * (x * x)
c == d

//  commutative operation
//def f(x: A, y: A) = if ( less(y, x) ) g(y, x) else g(x, y)
