#!/usr/bin/env python3

def URLify(string):
    string = string.replace(" ","%20")
    print(string)

URLify("hi test this")

def URLIfySecond(string):
    output = ""
    for char in string:
        if char == " ":
            output += "%20"
        else:
            output += char
    print(output)

URLIfySecond("hi test this")
