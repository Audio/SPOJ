loop do overhang = gets.to_f
  break if overhang == 0

  sum = 0
  n = 2.to_f
  while sum < overhang
    sum += (1 / n)
    n += 1
  end

  puts "#{n.to_i-2} card(s)"
end

