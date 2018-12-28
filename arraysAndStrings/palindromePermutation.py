#!/usr/bin/env python3

def palidromepermutation(string):
    string = string.lower().replace(" ","")
    charHash = {}
    for char in string:
        if char in charHash:
            charHash[char] = 0
        else:
            charHash[char] = 1
    if len(string) % 2 == 0:
        for _,v in charHash.items():
            if v != 0:
                return False
        return True
    else:
        flag = False
        for _,v in charHash.items():
            if v == 1:
                if flag:
                    return False
                else:
                    flag = True
        if not flag:
            return False
        return True

palidromepermutation("Tact Coa")
palidromepermutation("Tact Coaa")
palidromepermutation("Tact Coaaz")

