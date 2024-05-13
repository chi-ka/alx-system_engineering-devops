#!/usr/bin/env ruby

def match_school(string)
  regex = /School/
  matches = string.scan(regex)
  if matches.any?
    puts matches.join
  else
    puts ""
  end
end

match_school(ARGV[0])
