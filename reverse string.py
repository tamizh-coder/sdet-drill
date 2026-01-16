Approach 1: Built-in (Slicing)

def reverse_string(s):
    return s[::-1]

# Examples
print(reverse_string(""))      # ""
print(reverse_string("a"))     # "a"
print(reverse_string("hello")) # "olleh"



Approach 2: Manual Loop
def reverse_string_manual(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

# Examples
print(reverse_string_manual(""))      # ""
print(reverse_string_manual("a"))     # "a"
print(reverse_string_manual("hello")) # "olleh"

# for list  we can use the reverse() in built function
def rev_str(s):
return s.reverse()

#examples
print (rev_str(["a","b","c","d"))

my_string = "hello"
reversed_iterator = reversed(my_string)
reversed_string = "".join(reversed_iterator)
# reversed_string is "olleh"
# my_string is still "hello"

