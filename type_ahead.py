import re


def auto_suggest(words, subword):
    if '*' in subword:
        # Convert wildcard '*' to regex '.*'
        regex_pattern = re.escape(subword).replace(r'\*', '.*')
        pattern = re.compile(f'^{regex_pattern}$', re.IGNORECASE)
    else:
        # Create a regex pattern to match the subword as a substring
        regex_pattern = re.escape(subword)
        pattern = re.compile(f'.*{regex_pattern}.*', re.IGNORECASE)
    
    # Filter words that match the pattern
    matching_words = [word for word in words if pattern.match(word)]
    return matching_words

# Function to take input from the user
def get_user_input():
    words_input = input("Enter up to 5 words with similar spellings(Input1) : ")
    words = [word.strip() for word in words_input.split(',')]

    subword_input = input("Enter the part of the words(Input2): ")
    subword = subword_input.strip()

    return words, subword

# Example usage
if __name__ == "__main__":
    words, subword = get_user_input()
    matching_words = auto_suggest(words, subword)
    print("Matching sub_word (Output):", matching_words)
