def closestVowel(c: chr) -> chr:
    vowels = ["a", "e", "o", "u", "i"]
    output = 999
    output_char = ""
    for v in vowels:
        if abs(ord(c) - ord(v)) < output:
            output = ord(c) - ord(v)
            output_char = v
    return output_char


print(closestVowel("b"))
print(closestVowel("s"))
print(closestVowel("c"))
print(closestVowel("i"))
print(closestVowel("z"))
