def is_palindrome(phrase):
    if((phrase[0::1]) == (phrase[::-1])):
        return True
    else:
        return False