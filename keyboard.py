import random
import string

def generate_random_word(length):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

def keyboard_simulator(word_count, min_word_length, max_word_length):
    words = []
    for _ in range(word_count):
        word_length = random.randint(min_word_length, max_word_length)
        words.append(generate_random_word(word_length))
    return words

def main():
    word_count = int(input("Enter the number of words to generate: "))
    min_word_length = int(input("Enter the minimum length of a word: "))
    max_word_length = int(input("Enter the maximum length of a word: "))

    random_words = keyboard_simulator(word_count, min_word_length, max_word_length)
    print("Randomly generated words:", random_words)

if __name__ == '__main__':
    main()
