# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 00:22:10 2018

@author: Hi
"""

#Write a function called are_anagrams. The function should
#have two parameters, a pair of strings. The function should
#return True if the strings are anagrams of one another,
#False if they are not.
#
#Two strings are considered anagrams if they have only the
#same letters, as well as the same count of each letter. For
#this problem, you should ignore spaces and capitalization.
#
#So, for us: "Elvis" and "Lives" would be considered
#anagrams. So would "Eleven plus two" and "Twelve plus one".
#
#Note that if one string can be made only out of the letters
#of another, but with duplicates, we do NOT consider them
#anagrams. For example, "Elvis" and "Live Viles" would not
#be anagrams.


#Write your function here!
def are_anagrams(str_1, str_2):
    str_1_dict = {}
    str_2_dict = {}
    result = None
    for c in str_1:
        if c != " ":
            if c.upper() not in str_1_dict:
                str_1_dict[c.upper()] = 1
            else:
                str_1_dict[c.upper()] = str_1_dict[c.upper()] + 1
    for c in str_2:
        if c != " ":
            if c.upper() not in str_2_dict:
                str_2_dict[c.upper()] = 1
            else:
                str_2_dict[c.upper()] = str_2_dict[c.upper()] + 1
    if len(str_1_dict) == len(str_2_dict):
        for char in str_1_dict:
            if char in str_2_dict:
                if str_2_dict[char] == str_1_dict[char]:
                    result = True
                else:
                    result = False
            else:
                result = False
    else:
        result = False
    #print(str_1_dict, str_2_dict)
    return result
#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: True, False, True, False, each on their own line.
#print(are_anagrams("Elvis", "Lives"))
#print(are_anagrams("Elvis", "Live Viles"))
#print(are_anagrams("Eleven plus two", "Twelve plus one"))
#print(are_anagrams("Nine minus seven", "Five minus three"))
print(are_anagrams("Dormitory", "Dirty Room"))
