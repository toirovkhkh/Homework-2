def is_palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False


a = is_palindrome("лепсспел")
b = is_palindrome("helloworld")
print(a)
print(b)
