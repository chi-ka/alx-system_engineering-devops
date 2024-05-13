#!/usr/bin/env ruby

def extract_info(log_line)
  sender = log_line.match(/\ 
  receiver = log_line.match(/\ 
  flags = log_line.match(/\ 

  "#{sender},#{receiver},#{flags}"
end

def process_log(log_file)
  File.readlines(log_file).each do |line|
    if line.include?('Sent SMS') || line.include?('Receive SMS')
      puts extract_info(line)
    end
  end
end

if ARGV.empty?
  puts "Usage: #{$PROGRAM_NAME} <log_file>"
  exit 1
end

process_log(ARGV[0])
