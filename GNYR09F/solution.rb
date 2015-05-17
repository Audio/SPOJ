def solve n, k
  row1 = Array.new(k + 1, 0)
  row1[0] = 2
  row2 = Array.new(k + 1, 0)
  row2[0] = 3
  row2[1] = 1

  (2...n).each {|n|
    k.downto(1) {|j| row1[j] = row2[j] + row2[j - 1] + row1[j] - row1[j - 1]}
    row1[0] += row2[0]
    row1, row2 = row2, row1
  }

  row2[k]
end

gets # ignore first line
while (line = gets)
  ints = line.split
  i = ints[0]
  n = ints[1].to_i
  k = ints[2].to_i

  result = solve n, k
  puts "#{i} #{result}"
end

