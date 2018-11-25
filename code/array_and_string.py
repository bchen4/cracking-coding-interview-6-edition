#! /usr/local/bin/python3


def is_unique(s):
    """
    Determine if a string has all unique characters. What if you cannot use additional data structures?
    :param s: given string
    :return: True or False
    """
    if not s: # make sure s is not null
        unique = s[0]
        for i in s[1:]:
            if i in s[0]:
                return False
            else:
                unique += i
        return True
    else:
        return False


