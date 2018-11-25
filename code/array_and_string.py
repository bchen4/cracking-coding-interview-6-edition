#! /usr/local/bin/python3


def is_unique(s):
    """
    Determine if a string has all unique characters. What if you cannot use additional data structures?
    :param s: given string
    :return: True or False
    :bigO: N^2 since check current character in unique string is N
    """
    if len(s) > 0:  # make sure s is not null
        unique = s[0]
        for i in s[1:]:
            if i in unique:
                return False
            else:
                unique += i
        return True
    else:
        return False


def check_permutation(a, b):
    """
    Given two strings, write a method to decide if one is a permutation of the other.
    :param a: string
    :param b: string
    :return: True or False
    """
    if len(a) != len(b):
        return False
    else:  # Compare the count of each character in two strings
        for i in a:
            if a.count(i) != b.count(i):
                return False
        return True

def urlify(a, b):
    """
    Replace all spaces in a string with '%20'. Assume the string has sufficient
    space at the end to hold the additional characters.
    And you are given the true length of the string.

    Example input:  "Mr John Smith    ", 13
    Example output: "Mr%20John%20Smith"

    :param a:
    :param b: true length of the string
    :return:
    """
    new_string = ""
    for i in range(b):
        if a[i] != " ":
            new_string += a[i]
        else:
            new_string += "%20"
    return new_string