#!/usr/bin/env python3

def oneAway(arr):
    str1,str2 = arr[0],arr[1]
    if abs(len(str1) - len(str2)) > 1: return False
    j = 0
    for i in range(0,min(len(str1),len(str2))):
        if str1[i] != str2[j]:
            if str1[i+1:] != str2[j+1:] or str1[i+1:] != str2[j:] or str1[i:] != str2[j+1:]:
                return False
        j+=1
    return True

oneAway(["pale","pales"])
oneAway(["pales","pale"])
oneAway(["pale","paless"])
oneAway(["spale","paless"])