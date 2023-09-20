def mysplit(strng) -> list:
    my_list = []
    if strng.isspace():
        return my_list
    substring = ''
    for ch in strng:
        if ch.isspace() and len(substring.strip()) > 0:
            my_list.append(substring.strip())
            substring = ''
        else:
            substring += ch
    if len(substring.strip()) > 0:
        my_list.append(substring)
    return my_list


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
