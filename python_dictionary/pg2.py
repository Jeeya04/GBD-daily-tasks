# pg2: Count word frequency in a string

def word_frequency(sentence):
    words = sentence.split()
    freq = {}

    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    return freq


text = "the quick brown fox jumps over the lazy dog"
print(word_frequency(text))
