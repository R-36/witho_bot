def find_vowel(vowel_mas, text):
    count = 0
    for i in range(len(text)):
        for j in range(len(vowel_mas)):
            if text[i].lower() == vowel_mas[j]:
                count += 1
                break
    return count


def find_consonant(consonant_mas, text):
    count = 0
    for i in range(len(text)):
        for j in range(len(consonant_mas)):
            if text[i].lower() == consonant_mas[j]:
                count += 1
                break
    return count
