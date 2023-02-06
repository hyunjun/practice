# Enum.map [1, 2, 3, 4], fn x -> x + 2 end
# Enum.map [1, 2, 3, 4], fn x -> IO.inspect x end
l = [1, 2, 3, 4]
Enum.map l, &(&1 + 2)
Enum.map l, &(IO.inspect &1)
