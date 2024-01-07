#!/usr/bin/env ruby

sender = ARGV[0].match(/(?<=\[from:)[^\]]*(?=\])/)
receiver = ARGV[0].match(/(?<=\[to:)[^\]]*(?=\])/)
flags = ARGV[0].match(/(?<=\[flags:)[^\]]*(?=\])/)

puts "%s,%s,%s" % [sender, receiver, flags]
