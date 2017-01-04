def sum(f: Int => Int): (Int, Int) => Int = {
  def sumF(a: Int, b: Int): Int =
    if ( a > b ) 0
    else f(a) + sumF(a + 1, b)
  sumF
}

def fact(n: Int): Int =
  if ( n == 0 ) 1 else n * fact(n - 1)

def sumInts = sum(x => x)
def sumCubes = sum(x => x * x * x)
def sumFactorials = sum(fact)

def cube(x: Int): Int = x * x * x
sum (cube) (1, 10)
sumCubes(1, 10)

def product(f: Int => Int)(a: Int, b: Int): Int =
  if ( a > b ) 1  //  unit value
  else f(a) * product(f)(a + 1, b)
product(x => x * x)(3, 4)

def fact2(n: Int) = product(x => x)(1, n)
fact2(5)

def mapReduce(f: Int => Int, combine: (Int, Int) => Int, zero: Int)(a: Int, b: Int): Int =
  if ( a > b ) zero
  else combine(f(a), mapReduce(f, combine, zero)(a + 1, b))

def productMR(f: Int => Int)(a: Int, b: Int): Int =
  mapReduce(f, (x, y) => x * y, 1)(a, b)
productMR(x => x * x)(3, 4)

def sumMR(f: Int => Int)(a: Int, b: Int): Int =
  mapReduce(f, (x, y) => x + y, 0)(a, b)
sumMR(x => x)(1, 4)
