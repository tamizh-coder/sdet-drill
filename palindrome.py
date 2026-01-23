# Simple Loop

def is_palindrome(s):
       temp_list = []
    for char in s:
        if char.isalnum():         # 1. Letter illa Number-ah irundha mattum
            lower_char = char.lower() # 2. Adha chinna ezhutha mathu
            temp_list.append(lower_char) # 3. List-la sethuko
    
    clean_s = "".join(temp_list)   # 4. List-la irukkura ellathayum ottu
    return clean_s == clean_s[::-1]
# Example
print(is_palindrome("A man, a plan, a canal: Panama")) # True
print(is_palindrome("race a car"))                    # False




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

#number palindrome
num = int(input("Enter a number: "))

original = num
reverse = 0

while num != 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

if original == reverse:
    print("Palindrome")
else:
    print("Not a Palindrome")
