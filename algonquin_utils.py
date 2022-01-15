# Annie Kuo

# This program retrieves the pronounciation of an Algonquin word.

# define global variables
CONSONANTS = "bcdghkmnpstwyzj"
VOWELS = "aeio"
VOWELS_WITH_ACCENT = "àèìò"
PUNCTUATION = ',;:.?!-'
DIPHTHONGS = ['aw', 'ay', 'ew', 'ey', 'iw', 'ow']

# define functions

def is_valid_consonant(char):
    """ (str) -> bool

    The function returns if the input string is a single character representing a valid consonant in Algonquin.
    
    >>> is_valid_consonant('j')
    True
    >>> is_valid_consonant('x')
    False
    >>> is_valid_consonant('gh')
    False
    >>> is_valid_consonant('')
    False
    >>> is_valid_consonant('T')
    True
    """
    
    # check if the input is a single character
    if len(char) != 1:
        return False
    
    # make the input lowercase to remove case sensitivity
    char= char.lower()
    
    # check if the input is one of the consonants in Algonquin
    is_a_consonant= char in CONSONANTS
    return is_a_consonant
    


def is_valid_vowel(char):
    """ (str) -> bool

    The function returns if the input string is a single character representing a valid vowel in Algonquin.
    
    >>> is_valid_vowel('a')
    True
    >>> is_valid_vowel('ò')
    True
    >>> is_valid_vowel('E')
    True
    >>> is_valid_vowel('È')
    True
    >>> is_valid_vowel('ae')
    False
    >>> is_valid_vowel(' ')
    False
    >>> is_valid_vowel('x')
    False
    """
    # check if the input is a single character
    if len(char) != 1:
        return False
    
    # make the input lowercase to remove case sensitivity
    char= char.lower()
    
    # check if the input is one of the vowels in Algonquin
    is_a_vowel= (char in VOWELS) or (char in VOWELS_WITH_ACCENT)
    return is_a_vowel



def is_valid_diphthong(letters):
    """ (str) -> bool

    The function returns if the input string is a valid diphthong in Algonquin.
    
    >>> is_valid_diphthong('aw')
    True
    >>> is_valid_diphthong('eW')
    True
    >>> is_valid_diphthong('')
    False
    >>> is_valid_diphthong('a')
    False
    >>> is_valid_diphthong('i w')
    False
    """
    # check if the input is a single character
    if len(letters) != 2:
        return False
    
    # make the input lowercase to remove case sensitivity
    letters= letters.lower()
    
    # check if the input is one of the diphthongs in Algonquin
    for diphthong in DIPHTHONGS:
        if diphthong == letters:
            return True
    return False



def is_valid_single_word(word):
    """ (str) -> bool

    The function returns if the input string is a single word made up by valid letters in Algonquin.
    
    >>> is_valid_single_word('Kwey')
    True
    >>> is_valid_single_word('hello')
    False
    >>> is_valid_single_word('MakaDewà')
    True
    >>> is_valid_single_word('è,iw')
    False
    >>> is_valid_single_word('kwey kwey')
    False
    >>> is_valid_single_word('paw')
    True
    >>> is_valid_single_word('')
    False
    
    """
    # check if the input is a single word made of at least 1 character
    if len(word) < 1:
        return False
    
    # check if there is a punctuation or space character in the word
    for symbol in (PUNCTUATION + " "):
        if symbol in word:
            return False
    
    # check if the input is made up of valid letters in Algonquin
    for letter in word:
        if not (is_valid_consonant(letter) or is_valid_vowel(letter)):
            return False
    return True

    
    
def is_valid_phrase(phrase):
    """ (str) -> bool
    
    The function returns if the input string contains only valid letters in Algonquin,
    accepted punctuation marks, or space characters.
    
    >>> is_valid_phrase('hello')
    False
    >>> is_valid_phrase('Andi ejayan?')
    True
    >>> is_valid_phrase('Kichi-mìgwech gì mìzhyàng Nigigòg.')
    True
    >>> is_valid_phrase('Kichi_mìgwech gì mìzhyàng Nigigòg.')
    False
    >>> is_valid_phrase('Free')
    False
    >>> is_valid_phrase('  !? Kìzis')
    True
    """
    
    # isolate each word by locating the space and punctuation characters
    list_of_words = []
    beginning_of_word = 0
    
    while beginning_of_word < len(phrase)-1:
        # find the index at which there is a punctuation or space character
        for index in range(beginning_of_word, len(phrase)):
            if phrase[index] in (PUNCTUATION + " "):
                break
            
        # isolate word
        single_word= phrase[beginning_of_word : index]
        
        # add the isolated word to the list of words
        if single_word not in (PUNCTUATION + " "): # in case there are two or more consecutive punctuation characters
            list_of_words.append(single_word)
        beginning_of_word = index + 1
    
    # check if all words found in the phrase are valid words in Algonquin
    for word in list_of_words:
        if not is_valid_single_word(word):
            return False
    return True
