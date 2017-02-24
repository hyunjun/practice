/*
val f: String => String = { case "ping" => "pong" }
f("ping")
//f("abc")
 */
val f: PartialFunction[String, String] = { case "ping" => "pong" }
f.isDefinedAt("ping")
f.isDefinedAt("pong")
f("ping")

//  Lecture 1-2
//  ::  Cons
//  ++  Concatenation
val N = 3
for {
  x <- 2 to N
  y <- 2 to x
  if ( x % y == 0 )
} yield(x, y)
(2 to N) flatMap(x =>
  (2 to x) withFilter (y =>
    x % y == 0) map (y => (x, y)))
