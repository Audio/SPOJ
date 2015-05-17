ints = gets.strip.split
$N = ints[0].to_i
$M = ints[1].to_i

$fares = []
$lowestFare = 2_147_483_647

(0...$N).each { $fares << gets.strip.split.collect {|str| str = str.to_i} }

def dfs(row, column, price)
  price += $fares[row][column]
  row += 1 # next row
  if row == $N
    $lowestFare = price if $lowestFare > price
  else
    dfs(row, column - 1, price) if column > 0
    dfs(row, column, price)
    dfs(row, column + 1, price) if column < $M - 1
  end
end

(0...$M).each { |column| dfs(0, column, 0) }

puts $lowestFare

