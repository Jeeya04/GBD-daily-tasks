with open("sample.txt", "r") as src:
    with open("copy.txt", "w") as dest:
        dest.write(src.read())

print("File copied")
