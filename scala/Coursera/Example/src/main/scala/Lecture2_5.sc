class Rational(x: Int, y: Int)  {
  //  Lecture 2-6
  require(y != 0, "denominator must be non-zero") //  predefined function

  //  Lecture 2-6
  def this(x: Int) = this(x, 1) //  single argument constructor

  //  Lecture 2-6
  private def gcd(a: Int, b: Int): Int = if ( b == 0 ) a else gcd(b, a % b)
  private val g = gcd(x, y)

  //  Lecture 2-5
  //def numer = x
  //def denom = y

  //  Lecture 2-6
  //def numer = x / g
  //def denom = y / g
  //val numer: Int = x / g //  calculated once
  //val denom: Int = y / g
  val numer = x //  unsimplified version internally
  val denom = y

  /*
  def addRational(r: Rational, s: Rational): Rational =
    new Rational(r.numer * s.denom + s.numer * r.denom, r.denom * s.denom)

  def makeString(r: Rational) =
    r.numer + "/" + r.denom
  */

  //  Lecture 2-6
  //def add(that: Rational) =
  //  Lecture 2-7
  def + (that: Rational) =
    new Rational(numer * that.denom + that.numer * denom, denom * that.denom)

  //override def toString = numer + " / " + denom
  override def toString = { //  toString for unsimplified version
    val g = gcd(numer, denom)
    numer / g + " / " + denom / g
  }

  //  Lecture 2-6
  //def neg: Rational = new Rational(-numer, denom)
  //  Lecture 2-7
  def unary_- : Rational = new Rational(-numer, denom)

  //  Lecture 2-6
  //def sub(that: Rational) = add(that.neg)
  //  Lecture 2-7
  def - (that: Rational) = this + -that

  //  Lecture 2-6
  //  def less(that: Rational) = numer * that.denom < that.numer * denom
  //  Lecture 2-7
  def < (that: Rational) = numer * that.denom < that.numer * denom

  //  Lecture 2-6
  //  def max(that: Rational) = if ( this.less(that) ) that else this
  //  Lecture 2-7
  def max(that: Rational) = if ( this < that ) that else this

  def * (that: Rational) = new Rational(numer * that.numer, denom * that.denom)
}

/*
val x = new Rational(1, 2)
x.numer
x.denom

val y = new Rational(2, 3)
x.add(y)
*/
val x = new Rational(1, 3)
val y = new Rational(5, 7)
val z = new Rational(3, 2)
x.numer
x.denom
//x.add(y)
//x.sub(y).sub(z)

//  Lecture 2-6
//y.add(y)  //  70/49 > 10/7
// x.less(y)
x.max(y)

//val strange = new Rational(1, 0)
//strange.add(strange)  //  ArithmeticException
new Rational(2)


//  Lecture 2-7
new Rational(1, 2).numer
//  substitution  [1/x, 2/y][][new Rational(1, 2)/this]
//new Rational(1, 2).less(new Rational(2, 3))
new Rational(1, 2) < new Rational(2, 3)
//  substitution  [1/x, 2/y][new Rational(2, 3)/that][new Rational(1, 2)/this]
x + y
-y
x - y - z
x < y
x max y
x * x + y * y

//  ((a + b) ^? (c ?^ d)) less ((a ==> b) | c)