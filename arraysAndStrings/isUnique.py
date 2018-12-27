#!/usr/bin/env python3

def isUnique(str):
    checkHash = {}
    for i in range(0,len(str)):
        if str[i] in checkHash:
            return False
        else:
            checkHash[str[i]] = True
    return True


isUnique("asd")

def isUniqueNoSpace(str):
    for i in range(0,len(str)-1):
        for j in range(i+1,len(str)):
            if str[i] == str[j]:
                return False
    return True

isUniqueNoSpace("asda")