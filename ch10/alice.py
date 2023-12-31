filename = 'alice.txt'

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
else:
    # Count the approximate number of words in the file.
    contents = contents.replace("“", '"').replace("”", '"').replace("‘", "'").replace("’", "'")
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")

# The file alice.txt has about 29465 words.