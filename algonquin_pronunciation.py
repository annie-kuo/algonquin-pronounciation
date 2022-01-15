# Annie Kuo

# This program determines the pronunciation of an Algonquin word

#import module to be used later
from algonquin_utils import *

# define functions
def get_consonant_pronunciation(consonant):
    """ (str) -> str

    The function returns the pronunciation of the input consonant.
    If the input is not a valid consonant, it returns an empty string.
    
    >>> get_consonant_pronunciation('m')
    'M'
    >>> get_consonant_pronunciation('j')
    'GE'
    >>> get_consonant_pronunciation('l')
    ''
    >>> get_consonant_pronunciation('hello')
    ''
    >>> get_consonant_pronunciation('')
    ''
    >>> get_consonant_pronunciation('B')
    'B'
    >>> get_consonant_pronunciation('dJ')
    'J'
    """
    
    # check if the input is a valid consonant in Algonquin
    if consonant.lower() == "dj": # exception: only consonant with 2 characters
        return "J"
    elif not is_valid_consonant(consonant):
        return ""
    
    # retrieve the consonant's pronunciation
    if consonant not in ["j", "dj"]:
        pronunciation = consonant.upper()     
    else:
        pronunciation = "GE"
    
    # return the consonant's pronunciation
    return pronunciation
     


def get_vowel_pronunciation(vowel):
    """ (str) -> str

    The function returns the pronunciation of the input vowel.
    If the input is not a valid vowel, it returns an empty string.
    
    >>> get_vowel_pronunciation("a")
    'A'
    >>> get_vowel_pronunciation("À")
    'A'
    >>> get_vowel_pronunciation("oo")
    ''
    >>> get_vowel_pronunciation("Ì")
    'EE'
    >>> get_vowel_pronunciation("M")
    ''
    """

    # check if the input is a valid vowel in Algonquin
    if not is_valid_vowel(vowel):
        return ""
    
    # remove case sensitivity
    vowel = vowel.lower()
    
    # retrieve the consonant's pronunciation
    if vowel in ["a", "à"]:
        pronunciation = "A"
        
    elif vowel in ["e", "è"]:
        pronunciation = "E"
    
    elif vowel == "i":
        pronunciation = "I"
    
    elif vowel == "ì":
        pronunciation = "EE"
    
    elif vowel == "o":
        pronunciation = "U"
    
    else:
        pronunciation = "O"
    
    # return the consonant's pronunciation
    return pronunciation



def get_diphthong_pronunciation(diphthong):
    """ (str) -> str

    The function returns the pronunciation of the input diphthong.
    If the input is not a valid diphthong, it returns an empty string.
    
    >>> get_diphthong_pronunciation("ay")
    'EYE'
    >>> get_diphthong_pronunciation("EW")
    'AO'
    >>> get_diphthong_pronunciation("meh")
    ''
    >>> get_diphthong_pronunciation("a w")
    ''
    >>> get_diphthong_pronunciation("iw")
    'EW'
    """
    # check if the input is a valid diphthong in Algonquin
    if not is_valid_diphthong(diphthong):
        return ""
    
    # remove case sensitivity
    diphthong = diphthong.lower()
    
    # retrieve the diphthong's pronunciation
    if diphthong in ["aw", "ow"]:
        pronunciation = "OW"
        
    elif diphthong == "ay":
        pronunciation = "EYE"
    
    elif diphthong == "ew":
        pronunciation = "AO"
    
    elif diphthong == "ey":
        pronunciation = "AY"
    
    else:
        pronunciation = "EW"
    
    # return the consonant's pronunciation
    return pronunciation
    


def get_word_pronunciation(word):
    """ (str) -> str

    The function returns the pronunciation of the input word.
    If the input is not a valid word, it returns an empty string.
    
    >>> get_word_pronunciation('Miskwà')
    'MISKWA'
    >>> get_word_pronunciation('madjashin')
    'MAJASHIN'
    >>> get_word_pronunciation('shàshàgwandàn')
    'SHASHAGWANDAN'
    >>> get_word_pronunciation('nàbìNeyàBikà')
    'NABEENAYABIKA'
    >>> get_word_pronunciation('hello')
    ''
    >>> get_word_pronunciation('pòdjòng')
    'POJONG'
    """
    # check if the input is a valid word in Algonquin
    if not is_valid_single_word(word):
        return ""
    
    # retrieve the word's pronunciation
    pronunciation= ""
    index = 0

    while index < len(word):
        # find the letter(s)' pronunciation depending on its type
        if word[index:index+2].lower() in DIPHTHONGS :
            pronunciation += get_diphthong_pronunciation(word[index:index+2])
            index += 2
        elif word[index:index+2].lower() == 'dj':
            pronunciation += get_consonant_pronunciation(word[index:index+2])
            index += 2
        elif word[index].lower() in CONSONANTS:
            pronunciation += get_consonant_pronunciation(word[index])
            index += 1
        else:
            pronunciation += get_vowel_pronunciation(word[index])
            index += 1
            
    return pronunciation
    


def tokenize_sentence(sentence):
    """ (str) -> list

    The function returns a list containing strings representing all words, or sequences of punctuation marks and space characters.
    If the input is not a valid phrase, it returns an empty string.
    
    >>> tokenize_sentence("a sentence")
    ['a', ' ', 'sentence']
    >>> tokenize_sentence("not@a#sentence")
    []
    >>> tokenize_sentence('nàbìyen') # Hello
    ['nàbìyen']
    >>> tokenize_sentence('Kwey, anin eji-pimadizin?')
    ['Kwey', ', ', 'anin', ' ', 'eji', '-', 'pimadizin', '?']
    >>> tokenize_sentence("Andi ejayan?")
    ['Andi', ' ', 'ejayan', '?']
    
    """
    
    # check if the input is a valid phrase in Algonquin
    if not is_valid_phrase(sentence):
        return []
    
    # initialize variables
    list_of_strings = []
    word_start = 0
    
    # iterate through the input string until it has reached the end of it
    while word_start < len(sentence)-1:
        # iterate through the string until the character at index is a punctuation or space char
        for index in range(word_start, len(sentence)):
            if sentence[index] in (PUNCTUATION + " "):
                break
            
        # in case it did not find a punctuation or space character until the end of the sentence    
        if sentence[index] not in (PUNCTUATION + " "):
            list_of_strings += [sentence[word_start : ]]
            break
        
        # add word to the list of strings  
        list_of_strings += [sentence[word_start : index]]
        
        # add the punctuation or space character (at index) to the list of strings
        
        # in case the punctuation or space character is the last character of the sentence
        if index == len(sentence)-1:
            list_of_strings += [sentence[-1]]
            word_start = len(sentence)-1
            
        # in case there are two consecutive punctuation or space characters
        elif sentence[index+1] in (PUNCTUATION + " "):
            list_of_strings += [sentence[index: index+2]]
            word_start = index + 2
        else:
            list_of_strings += [sentence[index]]
            word_start = index + 1
        
    # return the list of strings
    return list_of_strings



def get_sentence_pronunciation(sentence):
    """ (str) -> str

    The function returns the pronunciation of the sentence.
    If the input is not a valid phrase, it returns an empty string.
    
    >>> get_sentence_pronunciation('nàbìNeyàBikà')
    'NABEENAYABIKA'
    >>> get_sentence_pronunciation('Andi ejayan?')
    'ANDI EGEEYEAN?'
    >>> get_sentence_pronunciation('Kwey, anin eji-pimadizin')
    'KWAY, ANIN EGEI-PIMADIZIN'
    >>> get_sentence_pronunciation("A random English sentence")
    ''
    """
    # check if the input is a valid phrase in Algonquin
    if not is_valid_phrase(sentence):
        return ''
    
    # separate the sentence into parts
    list_of_strings= tokenize_sentence(sentence)
    
    # find the pronunciation of each word
    pronunciation = ""
    
    for sentence_part in list_of_strings:
        part_pronunciation = get_word_pronunciation(sentence_part)
        
        if part_pronunciation == "":
            pronunciation += sentence_part
        else:
            pronunciation += part_pronunciation
    
    # return the pronunciation of the whole sentence
    return pronunciation

