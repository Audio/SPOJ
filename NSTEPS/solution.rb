gets # just ignore the first line

while (line = gets)
  ints = line.split
  x = ints[0].to_i
  y = ints[1].to_i

  if x == y or x - 2 == y
    x -= 1 if x.odd?
    puts x + y
  else
    puts 'No Number'
  end
end

