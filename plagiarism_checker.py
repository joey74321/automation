# plagiarism_checker.py

from difflib import SequenceMatcher


def calculate_similarity(input_text_one, input_text_two):
    """
    Calculate the similarity ratio between two texts using SequenceMatcher.

    :param input_text_one: First text for comparison.
    :param input_text_two: Second text for comparison.
    :return: Similarity ratio.
    """
    similarity_ratio = SequenceMatcher(None, input_text_one, input_text_two).ratio()
    return similarity_ratio


# Rest of the code...

if __name__ == "__main__":
    # Example usage:
    text_one = "This is a sample text."
    text_two = "This is a similar sample text."
    result = calculate_similarity(text_one, text_two)
    print(f"Similarity Ratio: {result}")
