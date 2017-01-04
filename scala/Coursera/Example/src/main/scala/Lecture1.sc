34 + 65
def radius = 10
def pi = 3.14159
radius * pi
(2 * pi) * radius

def square(x: Double) = x * x
square(2)
square(5 + 4)
square(square(4))

def sumOfSquares(x: Double, y: Double) = square(x) + square(y)

// def power(x: Double, y: Int): Double = ...

def loop: Int = loop

def test(x: Int, y: Int) = x * x
/*
call-by-value vs. call-by-name
for test(2, 3), test(3 + 4, 8), test(7, 2 * 4), test(3 + 4, 2 * 4)
 */

//  Lecture 1-3
def first(x: Int, y: Int) = x
//first(1, loop)  //  compare call-by-value vs. call-by-name

def constOne(x: Int, y: => Int) = 1 //  y: => Int means call-by-name
constOne(1 + 2, loop) //  constOne(3, loop), then returns 1
//constOne(loop, 1 + 2) //  constOne(loop, 1 + 2), recursively evaluates loop again and again

//  Lecture 1-4
def abs(x: Int): Int = if ( x >= 0 ) x else -x
//  short-circuit evaluation

val x2 = 2
val y2 = square(x2)

def loop2: Boolean = loop2
def x = loop2 //  OK
val y = loop2 //  infinite loop

def and(x: Boolean, y: Boolean) =
  if ( x ) y else false
//  and(false, loop2)

def and2(x: Boolean, y: => Boolean) =
  if (x) y else false
and2(false, loop2)

//  Lecture 1-5
def abs(x: Double) = if ( x < 0 ) -x else x

def sqrtIter(guess: Double, x: Double): Double =
  if ( isGoodEnough(guess, x) ) guess
  else sqrtIter(improve(guess, x), x)

def isGoodEnough(guess: Double, x: Double) =
//abs(guess * guess - x) < 0.001
  abs(guess * guess - x) / x < 0.001

def improve(guess: Double, x: Double) =
  (guess + x / guess) / 2

def sqrt(x: Double) = sqrtIter(1.0, x)

sqrt(2)
sqrt(4)
sqrt(1e-6)
sqrt(1e60)


