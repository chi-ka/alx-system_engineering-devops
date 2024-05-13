#!/usr/bin/env ruby

def match_school(string)
  regex = /h[a-z0-9]n/
  match = string.match(regex)
  if match
    puts match[0]
  else
    puts ""
  end
end

match_school(ARGV[0])
