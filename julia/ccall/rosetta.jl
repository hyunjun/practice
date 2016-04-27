function hello_c(n::Int)
buffer = zeros(Cchar, n)
val = ccall((:HelloWorld, "rosetta"), Csize_t,  # OSX
# val = ccall((:HelloWorld, "./rosetta"), Csize_t,  # Linux
                                      (Ptr{Cchar}, Csize_t),
                                      buffer, length(buffer))
val = convert(Int64, val)
string = bytestring(pointer(buffer))
val, string
end

@show hello_c(5)
@show hello_c(13)
@show hello_c(20)
