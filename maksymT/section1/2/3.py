word = input("enter a word: ")
palindrome = word[::-1]
print(palindrome)
print(word.upper())
if palindrome == word:
    print("palindrome: TRUE")
else :
    print("palindrome: FALSE")