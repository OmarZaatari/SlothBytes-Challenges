def checkTitle(s: str) -> bool:
    word_list = s.split(" ")
    for word in word_list:
        if not word[0].isupper():
            return False
    return True


print(checkTitle("A Mind Boggling Achievement"))
print(checkTitle("A Simple C++ Program!"))
print(checkTitle("Water is transparent"))
