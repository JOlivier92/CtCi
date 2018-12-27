#!/usr/bin/env python3

def checkPermutation(arr):
    str1 = "".join(sorted([letter for letter in arr[0]]))
    str2 = "".join(sorted([letter for letter in arr[1]]))
    if str1 != str2:
        return False
    return True

checkPermutation(["asd","dsa"])
checkPermutation(["dsaa","asd"])
checkPermutation(["aasd","dsas"])
checkPermutation(["aasd","dsaa  "])

def checkPermutationHash(arr):
    str1 = "".join([letter for letter in arr[0]])
    str2 = "".join([letter for letter in arr[1]])
    checkHash = {}

    for letter in str1:
        if letter in checkHash:
            checkHash[letter] += 1
        else:
            checkHash[letter] = 1
    for letter in str2:
        if letter in checkHash:
            checkHash[letter] -= 1
        else:
            return False
    for k,_ in checkHash.items():
        if checkHash[k] != 0:
            return False
    return True

checkPermutationHash(["asd","dsa"])
checkPermutationHash(["dsaa","asd"])
checkPermutationHash(["aasd","dsas"])
checkPermutationHash(["aasd","dsaa  "])