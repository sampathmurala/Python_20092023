fs = input("Enter first string: ")
ss = input("Enter second string: ")
def find_word(text, word):
    idx: int = 0
    for ch in fs:
        idx = ss.find(ch, idx)
        if idx == -1:
            return False
    return True


print("Yes" if find_word(ss, fs) else "No")
