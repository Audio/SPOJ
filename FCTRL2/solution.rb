def fact n
  return 1 if n < 2
  return n * (fact n-1)
end

i = 0
loop do line = gets
  break if !line
  i += 1
  next if i == 1

  n = line.to_i
  p fact n
end

