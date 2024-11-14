def isPalindrome(word):
    # Base case: A word with one or zero characters is a palindrome
    if len(word) <= 1:
        return True
    # Recursive case: Check if the first and last characters are the same
    if word[0] == word[-1]:
        # Recurse on the substring that excludes the first and last characters
        return isPalindrome(word[1:-1])
    # If the first and last characters don't match, it's not a palindrome
    return False

# Example usage
words = ["gag", "pop", "hannah", "rotator", "example"]
for word in words:
    result = isPalindrome(word)
    print(f"{word} is a palindrome: {result}")
