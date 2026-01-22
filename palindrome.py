#list comprehensions or Generator Expression
def is_palindrome(s):
    # Step 1: Filter alphanumeric and convert to lowercase
    # Oru line-la clean panna slicing logic
    clean_s = "".join(char.lower() for char in s if char.isalnum())
    
    # Step 2: Compare with reverse
    return clean_s == clean_s[::-1]

# Example
print(is_palindrome("A man, a plan, a canal: Panama")) # True
print(is_palindrome("race a car"))                    # False
