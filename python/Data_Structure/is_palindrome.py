def is_palindrome(word: str) -> bool:
    left: int = 0
    right: int = len(word)-1

    while(left < right):
        if(word[left] != word[right]):

            return False
        
        left += 1
        right -= 1

    return True


# Test code
words = ["racecar", "rotor", "tomato", "별똥별", "코끼리"]
for word in words:
    print("Is '%s' palindrome?  %s" % (word, is_palindrome(word)))
