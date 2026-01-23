with open("sample.txt", "r") as f:
    data = f.read()

lines = data.split("\n")
words = data.split()
chars = len(data)

print("Lines:", len(lines))
print("Words:", len(words))
print("Characters:", chars)
