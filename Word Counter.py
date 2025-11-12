import re
from collections import Counter

def count_unique_words(text):

    text = text.lower()

# regex
    words = re.findall(r"[A-Za-z0-9']+", text)

#each word
    word_counts = Counter(words)

#Unique
    unique_count = len(word_counts)

#result
    print("\n--- Result ---")
    print(f"Total words: {len(words)}")
    print(f"Unique words: {unique_count}")
    print("\nWord Frequencies:")
    for word, count in word_counts.items():
        print(f"{word}: {count}")

#main
if __name__ == "__main__":
    text = input("Enter your text:\n")
    count_unique_words(text)
