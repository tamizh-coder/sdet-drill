def is_valid(s):
    stack = []
    mapping = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for char in s:
        # If closing bracket
        if char in mapping:
            # Stack empty or mismatch
            if not stack or stack.pop() != mapping[char]:
                return False
        else:
            # Opening bracket
            stack.append(char)

    # Stack should be empty at the end
    return len(stack) == 0


# User input
if __name__ == "__main__":
    s = input("Enter brackets string: ")
    print(is_valid(s))

