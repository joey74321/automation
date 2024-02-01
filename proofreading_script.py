# proofreading_script.py

import nltk
from nltk import word_tokenize
from spellchecker import SpellChecker

nltk.download('punkt')


def create_custom_dictionary():
    """
    Creates a custom dictionary with known words.
    """
    known_words = ["'m", "'s", "'re", "'ve", "'ll", "'d", "n't", "i'm"]
    custom_dict = set(known_words)
    return custom_dict


def proofreading_function(text):
    """
    Proofreads the given text and identifies potential errors.
    """
    # Tokenize the text into words
    words_to_check = word_tokenize(text.lower())

    # Remove punctuation from the list of words
    words_to_check = [word for word in words_to_check if word.isalnum()]

    # Create a custom set with known words
    custom_dict = create_custom_dictionary()

    # Initialize SpellChecker
    spell = SpellChecker()

    # Ignore words in the custom dictionary
    spell.word_frequency.load_words(custom_dict)

    # Identify potential errors, ignoring hyphenated words
    misspelled = [word for word in words_to_check if '-' not in word and word not in custom_dict and word not in spell]

    return misspelled


# Example usage:
if __name__ == "__main__":
    # Get user input for the text to be proofread
    user_input = input("Enter a sentence or paragraph for proofreading: ")

    # Call the proofreading function with user input
    proofreading_result = proofreading_function(user_input)

    # Print the potential errors
    print("Potential misspelled errors:", proofreading_result)
