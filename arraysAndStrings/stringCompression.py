#!/usr/bin/env python3

def stringCompression(string):
    if len(string) <= 1:
        return string
    output = string[0]
    counter = 1
    for char in string[1:]:
        if char == output[-1]:
            counter += 1
        else:
            output += str(counter) + char
            counter = 1
    output += str(counter)

    if len(output) < len(string):
        return output
    return string

stringCompression("aabcccccaaa")
stringCompression("aaaaaaaa")
stringCompression("abcdefg")