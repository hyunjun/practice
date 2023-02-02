print_fizz_buzz = fn
  (0, 0, _) -> "FizzBuzz"
  (0, _, _) -> "Fizz"
  (_, 0, _) -> "Buzz"
  (_, _, a) -> a
end

IO.puts print_fizz_buzz.(0, 0, 0)
IO.puts print_fizz_buzz.(0, 0, 10)
IO.puts print_fizz_buzz.(0, 10, 10)
IO.puts print_fizz_buzz.(10, 0, 10)
IO.puts print_fizz_buzz.(10, 10, 10)

fizz_buzz = fn (n) -> print_fizz_buzz.(rem(n, 3), rem(n, 5), n) end

for n <- 10..16 do
  IO.puts fizz_buzz.(n)
end
