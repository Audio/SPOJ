gets # just ignore the first line

$empty_seqs = {'TTT' => 0, 'TTH' => 0, 'THT' => 0, 'THH' => 0, 'HTT' => 0, 'HTH' => 0, 'HHT' => 0, 'HHH' => 0}

def count seq
  count = $empty_seqs.clone
  (2...40).each { |i| count[ seq[i-2..i] ] += 1 }

  count
end

while (i = gets)
  seq = gets.strip
  result = count seq
  puts "#{i.strip} #{result.values.join(' ')}"
end

