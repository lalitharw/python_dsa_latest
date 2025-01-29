def isPalindrome(str) -> str:
    str = str.replace(" ",'').lower()
    left = 0
    right = len(str) - 1

    # return str

    while left <= right:
        if str[left].lower() != str[right].lower():
            return False
        
        left += 1
        right -= 1
        
    return True
    
print(isPalindrome('Was it a car or a cat I saw'))
print(isPalindrome('tab a cat'))