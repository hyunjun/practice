import scala.io.Source

val in = Source.fromURL("https://github.com/frankh/coursera-scala/blob/master/forcomp/src/main/resources/forcomp/linuxwords.txt")
val words = in.getLines.toList filter (word => word forall (chr => chr.isLetter))
val mnemonics = Map('2' -> "ABC", '3' -> "DEF", '4' -> "GHI", '5' -> "JKL",
                    '6' -> "MNO", '7' -> "PQRS", '8' -> "TUV", '9' -> "WXYZ")
val charCode: Map[Char, Char] = //Map('A' -> '2', 'B' -> '2', ...)
  for ( (digit, str) <- mnemonics; ltr <- str ) yield ltr -> digit
def wordCode(word: String): String =
  word.toUpperCase map charCode
wordCode("JAVA")
wordCode("Java")
val wordsForNum: Map[String, Seq[String]] =
  words groupBy wordCode withDefaultValue Seq()
def encode(number: String): Set[List[String]] =
  if ( number.isEmpty ) Set(List())
  else
    (for {
      split <- 1 to number.length
      word <- wordsForNum(number take split)
      rest <- encode(number drop split)
    } yield word :: rest).toSet
encode("7225247386")
def translate(number: String): Set[String] =
  encode(number) map (_ mkString " ")