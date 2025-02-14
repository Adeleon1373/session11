#find three letter words starting with b inside file


punctuation = ",.?!':;\"" #punctuation we want to get rid of
def find_words(filename):
    """
    Prints 3 letter words starting with b from a file
    :param filename: the name of the file
    :return: None
    """
    with open(filename) as f:
        for line in f:
            for p in punctuation:
                line = line.replace(p,"")
            words = line.split()
            for word in words:
                if len(word) == 3 and word[0] in "bB":
                    print(word)

find_words("input.txt")
