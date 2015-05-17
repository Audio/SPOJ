while (code = gets)
  if not code.match(/^[a-z]+([A-Z][a-z]*)*$/).nil?
    puts code.gsub(/([A-Z])/) { |s| "_#{s.downcase}" }
  elsif not code.match(/^[a-z]+(_[a-z]+)*$/).nil?
    puts code.gsub(/_(.)/) { |s| s[1].upcase }
  else
    puts 'Error!'
  end
end

