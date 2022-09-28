WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    """
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = inFile.read().split()
    print("  ", len(wordList), "words loaded.")
    return wordList


def isWord(wordList, word):
    """
    Determines if word is a valid word.
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in wordList


def randomWord(wordList):
    """
    Returns a random word.
    """
    return random.choice(wordList)


def randomString(wordList, n):
    """
    Returns a string containing n random words from wordList
    """
    return " ".join([randomWord(wordList) for _ in range(n)])


def randomScrambled(wordList, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.
    """
    s = randomString(wordList, n) + " "
    shifts = [(i, random.randint(0, 25)) for i in range(len(s)) if s[i-1] == ' ']
    return applyShift(s, shifts)[:-1]


def getStoryString():
    """
    Returns a story in encrypted text.
    """
    return open("story.txt", "r").read()


def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value == 0 <= int < 26
    """
    original = string.ascii_lowercase
    xi_string = original[shift:26] + original[:shift]
    return xi_string


def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.
    """
    original = string.ascii_lowercase
    word = ''
    for i in text:
        if i in coder:
            word += (coder[original.index(i)])
        elif i in coder.upper():
            word += (coder.upper()[original.upper().index(i)])
        else:
            word += (text[text.index(i)])
    return word


def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar xi by the given shift offset. Lower case letters shall remain
    lower case, upper case letters shall remain upper case, and all other punctuation shall stay as it is.
    """
    return applyCoder(text, buildCoder(shift))


def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.
    """
    best, count = None, 0
    for xi in range(26):
        goal = []
        for i in text:
            if isWord(wordList, applyShift(i, xi)):
                goal.append(applyShift(i, xi))
        if len(goal) > count:
            best, count = xi, len(goal)
    return best


def decryptStory():
    """
    decrypt the story given by the function getStoryString()
    """
    return applyShift(getStoryString(), findBestShift(wordList, getStoryString().split()))


if __name__ == '__main__':
    # To test findBestShift:
    wordList = loadWords()
    # s = applyShift('Hello, world!', 8)
    # bestShift = findBestShift(wordList, s)
    # assert applyShift(s, bestShift+2) == 'Hello, world!'
    # To test decryptStory, comment the above four lines and uncomment this line:
    print(decryptStory())

