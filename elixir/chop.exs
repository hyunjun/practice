defmodule Chop do
  def guess(actual, actual..actual) do
    IO.puts actual
  end

  def guess(actual, l..r) do
    IO.puts "#{actual} #{l} #{r}"
    m = div(l + r, 2)
    '''
    if actual < m do
      guess(actual, l..m)
    end
    if m < actual do
      guess(actual, m..r)
    end
    if m == actual do
      guess(actual, actual..actual)
    end
    '''
    cond do
      actual < m -> guess(actual, l..m)
      m < actual -> guess(actual, m..r)
      actual == m -> guess(actual, actual..actual)
    end
  end
end
