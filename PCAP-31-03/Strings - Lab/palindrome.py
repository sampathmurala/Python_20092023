text = input("Enter text: ")
if text.lower().replace(" ", "") == text[::-1].lower().replace(" ", ""):
    print("It's a palindrome")
else:
    print("It is not a palindrome")
