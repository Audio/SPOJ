friends = []
friendsOfFriends = []

i = 0
loop do line = gets
  break if !line
  i += 1
  next if i == 1

  ids = line.split(' ')
  friends << ids[0]
    
  ids.slice!(0, 2)
  friendsOfFriends.concat(ids)
end

friends.uniq!
friendsOfFriends.uniq!

puts (friendsOfFriends - friends).size

