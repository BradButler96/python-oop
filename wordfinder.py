from random import randint, random

"""Word Finder: finds random words from a dictionary."""


class WordFinder:
    ...
    
    def __init__(self, file):
        self.file = file
        return self.count_words()

    def count_words(self):
        f = open(self.file).readlines()
        print(f'{len(f)} words read')

    def random(self):
        f = open(self.file).readlines()       
        random_num = randint(0, len(f) - 1)
        random_word = f[random_num]
        random_word.rstrip('\n')
        return random_word
        
        
class SpecialWordFinder(WordFinder):

    def __init__(self, file):
        super().__init__(file)

    def random(self):
        with open(self.file) as f:
            f_read = [word for word in f.readlines() if word[0] != '#' and word != '\n']
            random_num = randint(0, len(f_read) - 1)
            random_word = f_read[random_num].rstrip('\n')
            return random_word
