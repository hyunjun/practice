val romanNumerals = Map("I" -> 1, "V" -> 5, "X" -> 10)
val capitalOfCountry = Map("US" -> "Washington", "Switzerland" -> "Bern")

//  Maps are Functions
capitalOfCountry("US")
//capitalOfCountry("Andorra")

//  Option type
capitalOfCountry get "US"
capitalOfCountry get "Andorra"

def showCapital(country: String) = capitalOfCountry.get(country) match {
  case Some(capital) => capital
  case None => "missing data"
}
showCapital("US")
showCapital("Andorra")

val fruit = List("apple", "pear", "orange", "pineapple")
fruit sortWith (_.length < _.length)
fruit.sorted
fruit groupBy (_.head)

//  Map Example, polynomial
//  x^3 - 2x + 5
Map(0 -> 5, 1 -> -2, 3 -> 1)
class Poly(val terms: Map[Int, Double]) {
  def + (other: Poly) = new Poly(terms ++ (other.terms map adjust))
  def adjust(term: (Int, Double)): (Int, Double) = {
    val (exp, coeff) = term
    terms get exp match {
      case Some(coeff1) => exp -> (coeff + coeff1)
      case None => exp -> coeff
    }
  }
  override def toString =
    (for ( (exp, coeff) <- terms.toList.sorted.reverse ) yield coeff + "x^" + exp) mkString " + "
}
val p1 = new Poly(Map(1 -> 2.0, 3 -> 4.0, 5 -> 6.2))
val p2 = new Poly(Map(0 -> 3.0, 3 -> 7.0))
p1 + p2

//  Default values
val cap1 = capitalOfCountry withDefaultValue "<unknown>"
cap1("Andorra")

class Poly2(val terms0: Map[Int, Double]) {
  val terms = terms0 withDefaultValue 0.0
  def +(other: Poly2) = new Poly2(terms ++ (other.terms map adjust))
  def adjust(term: (Int, Double)): (Int, Double) = {
    val (exp, coeff) = term
    exp -> (coeff + terms(exp))
  }
  override def toString =
    (for ( (exp, coeff) <- terms.toList.sorted.reverse ) yield coeff + "x^" + exp) mkString " + "
}
val p11 = new Poly2(Map(1 -> 2.0, 3 -> 4.0, 5 -> 6.2))
val p21 = new Poly2(Map(0 -> 3.0, 3 -> 7.0))
p11 + p21

//  repeated parameters
class Poly3(val terms0: Map[Int, Double]) {
  def this(bindings: (Int, Double)*) = this(bindings.toMap)
  val terms = terms0 withDefaultValue 0.0
  def +(other: Poly3) = new Poly3(terms ++ (other.terms map adjust))
  def adjust(term: (Int, Double)): (Int, Double) = {
    val (exp, coeff) = term
    exp -> (coeff + terms(exp))
  }
  override def toString =
    (for ( (exp, coeff) <- terms.toList.sorted.reverse ) yield coeff + "x^" + exp) mkString " + "
}
val p12 = new Poly3(1 -> 2.0, 3 -> 4.0, 5 -> 6.2)
val p22 = new Poly3(0 -> 3.0, 3 -> 7.0)
p12 + p22
p12.terms(7)

class Poly4(val terms0: Map[Int, Double]) {
  def this(bindings: (Int, Double)*) = this(bindings.toMap)
  val terms = terms0 withDefaultValue 0.0
  def +(other: Poly4) = new Poly4((other.terms foldLeft terms)(addTerm))
  def addTerm(terms: Map[Int, Double], term: (Int, Double)): Map[Int, Double] = {
    val (exp, coeff) = term
    terms + (exp -> (coeff + terms(exp)))
  }
  override def toString =
    (for ( (exp, coeff) <- terms.toList.sorted.reverse ) yield coeff + "x^" + exp) mkString " + "
}
val p13 = new Poly4(1 -> 2.0, 3 -> 4.0, 5 -> 6.2)
val p23 = new Poly4(0 -> 3.0, 3 -> 7.0)
p13 + p23

//  Final
class Polynom(val terms: Map[Int, Double]) {
  def + (other: Polynom) = new Polynom(terms ++ (other.terms map addTerm))
  private def addTerm(term: (Int, Double)) = {
    val (degree, coeff) = term
    degree -> (coeff + terms(degree))
  }
  override def toString = {
    val termStrings =
      for ( (pos, value) <- terms.toList.sorted.reverse ) yield value + "x^" + pos
    termStrings mkString " + "
  }
}
def Polynom(bindings: (Int, Double)*) =
  new Polynom(bindings.toMap withDefaultValue 0)
val p14 = Polynom(1 -> 2.0, 3 -> 4.0, 5 -> 6.2)
val p24 = Polynom(0 -> 3.0, 3 -> 7.0)
p14 + p24
