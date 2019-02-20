STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with', ' '
]

letters = "abcdefghijklmnopqrstuvwxyz "
letters = letters + letters.upper()

def clean_text(text):
    #Removing punctuation, ends with list of words
    text_with_spaces = ""
    for i in text:
        if i in letters:
            text_with_spaces = text_with_spaces + i
    text_with_spaces.replace("\n", " ")
    text_with_spaces = text_with_spaces.lower()
    return text_with_spaces.split(" ")

def print_word_freq(filename):
    """Read in `file` and print out the frequency of words in that file."""

    with open(filename) as file:
        text = file.read()
        text = clean_text(text)
    #Count word frequency in word list 
        word_count = {}   
        for i in text:
            if i not in word_count and i not in STOP_WORDS:
                word_count[i] = 1
            elif i not in STOP_WORDS:
                word_count[i] += 1
        
        #Sorts the dictionary by frequency value and prints first ten members
        # import pdb; pdb.set_trace()
        sorted_words = sorted(word_count.items(), key=lambda kv: kv[1], reverse=True)

        i = 0
        while i < 10:
            print(f"{sorted_words[i][0]} :: {sorted_words[i][1]} {'*' * sorted_words[i][1]}")
            i += 1


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
