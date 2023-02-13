# https://leetcode.com/problems/palindrome-number/

defmodule Solution do
  # runtime; 26.19%
  # memory; 88.9%
  @spec is_palindrome(x :: integer) :: boolean
  def is_palindrome(x) do
    Integer.to_string(x) == Integer.to_string(x) |> String.reverse
  end
end

data = [{121, true},
        {-121, false},
        {10, false},
        ]
for {x, expect} <- data do
  real = Solution.is_palindrome(x)
  IO.puts "#{x} expect #{expect} real #{real} result #{expect == real}"
end