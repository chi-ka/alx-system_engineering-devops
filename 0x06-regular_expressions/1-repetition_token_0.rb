#!/usr/bin/env ruby

def match_school(string)
  regex = /hbt{1,5}n/
  match = string.match(regex)
  if match
    puts match[0]
  else
    puts ""
  end
end

match_school(ARGV[0])
