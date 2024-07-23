char=input("Enter String:")
reverse=char[::-1]
print("Character:",char)
if char==reverse:
    print(char,"palindrome")
else:
    print(char," Is not a Palindrome")
