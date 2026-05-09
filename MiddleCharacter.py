#Program Find Middle Character

word = input("Enter a word: ")

mid = len(word)//2
new = word[mid-1 : mid+2]
print("The middle characters are", new)