#!/usr/bin/env ruby

def match_capital_letters(string)
  regex = /[A-Z]/
  matches = string.scan(regex)
  if matches.any?
    puts matches.join
  else
    puts ""
  end
end

match_capital_letters(ARGV[0])
