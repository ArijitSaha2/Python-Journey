# Write a function reverse_string(s) that returns the reverse of the string s.

def reverse_string(s):
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]

# Example usage:
input_str = "hello"
print(reverse_string(input_str))  # Output: "olleh"