//validate parathesis

function isValid(s) {
    const stack = [];
    const map = {
        ')': '(', 
        '}': '{',
        ']': '['
    };

    for (const char of s) {
        // If closing bracket
        if (char in map) {
            // Pop and compare
            if (stack.pop() !== map[char]) {
                return false;
            }
        } 
        // Opening bracket
        else {
            stack.push(char);
        }
    }

    // Stack must be empty at the end
    return stack.length === 0;
}

