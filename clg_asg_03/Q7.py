def check_vowels_consonants(ch):
    if len(ch) > 1:
        return "Not a character"
    if ch.lower() in ['a' or 'e' or 'i' or 'o' or 'u']:
        return "Vowel"
    else:
        return "Consonant"

ch = check_vowels_consonants("A")
print(ch)
