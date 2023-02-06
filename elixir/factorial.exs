defmodule Factorial do
  def of(0), do: 1
  def of(n), do: n * of(n - 1)
end

defmodule BadFactorial do
  def of(n), do: n * of(n - 1)
  def of(0), do: 1
end

defmodule Sum do
  def calc(0), do: 0
  def calc(n), do: n + calc(n - 1)
end

defmodule Gcd do
  def calc(x, 0), do: x
  def calc(x, y), do: calc(y, rem(x, y))
end
