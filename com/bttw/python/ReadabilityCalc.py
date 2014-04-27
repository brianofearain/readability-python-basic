from __future__ import print_function, division
import re

#These libraries are for the syllable counter
import nltk 
from nltk.corpus import cmudict 
import curses 
from curses.ascii import isdigit 


def main():
    pass

if __name__== '__main__': 
    main()


def sentence_parser(input):
    '''Split input into a list of sentences'''
    #Remove whitespace
    input = non_letter_remover(input)
    #Split along fullstops
    sentences = input.split('.')
    return sentences

	
def non_letter_remover(input):
    '''Replace all chars that are not letters in input with whitespace'''
    #This regex will remove punctuation (except fullstops), special chars, and numbers
    #Future versions should distinguish between decimal points and fullstops
    #Future versions should also distinguish between fullstops that delimit sentences and fullstops which designate letters of an acronym (like 'U.S.')
    regex = re.compile('[^A-Za-z. ]')
    return regex.sub(" ", input)	
	
def avg_letters_per_word(input):
    '''Determine the avg number of letters per word in the input'''
    #Create a list of all the words in the input
    words_list = input.split()
    word_count = len(words_list)
    char_count = 0
    for word in words_list:
        char_count += len(word)
    return char_count/word_count
	
	
def avg_sentences_per_word(input):
    '''Determine the avg number of sentences per word in a input'''
    
    sentences_list = sentence_parser(input)
    sentence_count = len(sentences_list)
    word_count = 0
    for sentence in sentences_list:
        word_count += len(sentence.split())
    return sentence_count/word_count


def avg_words_per_sentence(input):
    return 1/avg_sentences_per_word(input)






d = cmudict.dict() 
def count_syllables(word): 
  return [len(list(y for y in x if isdigit(y[-1]))) for x in d[word.lower()]] 

def flesh_kincaid(input):
    
    avg_words = avg_words_per_sentence(input)
    avg_sentences = avg_syllables_per_word(input)
    return .39 * avg_words + 11.8 * avg_sentences - 15.59

def coleman_liau(input):
    avg_letters = avg_letters_per_word(input)
    avg_sentences = avg_sentences_per_word(input)
    L = 100 * avg_letters
    S = 100 * avg_sentences
    return .0588 * L - .296 * S - 15.8




