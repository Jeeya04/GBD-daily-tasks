# pg1: Find words longer than 5 characters and alternate capitalization

def long_words_with_alt_case(sentence):
    words = sentence.split()
    result = []

    for word in words:
        if len(word) > 5:
            new_word = ""
            for i in range(len(word)):
                if i % 2 == 0:
                    new_word += word[i].upper()
                else:
                    new_word += word[i].lower()
            result.append(new_word)

    return result


text = "The quick brown fox jumps over the lazy dog"
print(long_words_with_alt_case(text))
