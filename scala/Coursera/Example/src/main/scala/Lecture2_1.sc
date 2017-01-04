def sumInts(a: Int, b: Int): Int =
  if ( a > b ) 0 else a + sumInts(a + 1, b)

def cube(x: Int): Int = x * x * x

def sumCubes(a: Int, b: Int): Int =
  if ( a > b ) 0 else cube(a) + sumCubes(a + 1, b)

def fact(n: Int): Int =
  if ( n == 0 ) 1 else n * fact(n - 1)

def sumFactorials(a: Int, b: Int): Int =
  if ( a > b ) 0 else fact(a) + sumFactorials(a + 1, b)

def sum(f: Int => Int, a: Int, b: Int): Int =
  if ( a > b ) 0
  else f(a) + sum(f, a + 1, b)

def id(x: Int): Int = x

def sumInts2(a: Int, b: Int) = sum(id, a, b)
def sumCubes2(a: Int, b: Int) = sum(cube, a, b)
def sumFactorials2(a: Int, b: Int) = sum(fact, a, b)

(x: Int) => x * x * x
(x: Int, y: Int) => x + y

def sumInts3(a: Int, b: Int) = sum(x => x, a, b)
def sumCubes3(a: Int, b: Int) = sum(x => x * x * x, a, b)

sumInts(1, 3)
sumCubes(1, 3)

//  tail recursive version of sum
def sum2(f: Int => Int)(a: Int, b: Int): Int = {
  def loop(a: Int, acc: Int): Int = {
    if ( a > b )
      acc
    else
      loop(a + 1, f(a) + acc)
  }
  loop(a, 0)
}
sum2(x => x)(1, 3)
sum2(x => x * x * x)(1, 3)
