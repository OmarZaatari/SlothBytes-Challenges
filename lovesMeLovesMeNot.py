def loveMeLoveMeNot(n: int) -> str:

    if n == 0:
        return "LOVES ME"

    output = ""
    i = 1
    while i <= n - 1:
        if i % 2 == 0:
            output += "Loves me not,"
        else:
            output += "Loves me,"
        i += 1
    i += 1
    output += "LOVES ME" if i % 2 == 0 else "LOVES ME NOT"
    return output


print("lovesMe(3):", loveMeLoveMeNot(3))  # Loves me,Loves me not,LOVES ME
print("")
print("lovesMe(6):", loveMeLoveMeNot(6))  # Loves me,Loves me not,Loves me,Loves me not,Loves me,LOVES ME NOT
print("")
print("lovesMe(1):", loveMeLoveMeNot(1))  # LOVES ME
