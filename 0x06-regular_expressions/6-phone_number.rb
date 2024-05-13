#!/usr/bin/env ruby

def match_phone_number(string)
  regex = /^\d{10}$/
  if regex.match?(string)
    puts string
  else
    puts ""
  end
end

match_phone_number(ARGV[0])
