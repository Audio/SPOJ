def sum array
  sum = 0
  array.each {|item| sum += item.reverse!.to_i}
  sum.to_s.reverse!.to_i
end

i = 0
loop do line = gets
  break if !line
  i += 1
  next if i == 1

  ints = line.split
  puts sum ints
end

