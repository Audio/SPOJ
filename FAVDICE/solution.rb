gets  # ignore first line

$cache = Array.new(1000)

while (n = gets)
  n = n.to_f
  if $cache[n-1].nil?
    chance = 0
    (1..n).each {|side| chance += n / side}
    $cache[n-1] = chance.round(2)
  end

  puts '%.2f' % $cache[n-1]
end

