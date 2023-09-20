def are_anagrams(s1: str, s2: str) -> bool:
    return sorted(s1.replace(" ", "")) == sorted(s2.replace(" ", ""))


text1 = input("Enter text1: ")
text2 = input("Enter text2: ")
print(text1, ",", text2, end=" ")
if are_anagrams(text1, text2):
    print("are Anagrams.")
else:
    print("are not Anagrams")

'''
text1 = input("Enter text1: ")
text2 = input("Enter text2: ")
if sorted(text1.replace(" ", "")) == sorted(text2.replace(" ", "")):
    print("Anagrams")
else:
    print("Not Anagrams")
'''