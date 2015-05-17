$exps = Array.new(12)
$exps[0] = 5
(1...12).each {|i| $exps[i] = $exps[i-1] * 5}

def z n
  return 0 if n < 5

  k = Math.log(n, 5).floor

  sum = 0
  (1..k).each {|i| sum += n / $exps[i-1]}

  sum
end

i = 0
loop do line = gets
  break if !line
  i += 1
  next if i == 1

  puts z line.to_i
end

