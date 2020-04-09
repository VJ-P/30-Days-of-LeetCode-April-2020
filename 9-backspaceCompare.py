# Given two strings S and T, return if they are equal when both are typed into empty text editors.
# '#' means a backspace character.

# Examples:

# Input: S = "ab#c", T = "ad#c"
# Output: true
# Explanation: Both S and T become "ac".

# Input: S = "ab##", T = "c#d#"
# Output: true

# Input: S = "a##c", T = "#a#c"
# Output: true

# Input: S = "a#c", T = "b"
# Output: false

def backspaceCompare(S, T):
    def rmBackspace(string):
        stack = []
        for char in string:
            if char == '#':
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(char)
        return stack
    str1 = rmBackspace(S)
    str2 = rmBackspace(T)
    if str1 == str2:
        return True
    else: 
        return False


# print(backspaceCompare('ab#c', 'ad#c'))
# print(backspaceCompare('a#c', 'b'))
# print(backspaceCompare('ab##', 'c#d#'))