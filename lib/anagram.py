# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = sorted(word.lower())

    def match(self, possible_anagrams):
        matches = []
        for possible_anagram in possible_anagrams:
            if sorted(possible_anagram.lower()) == self.word:
                matches.append(possible_anagram)
        return matches
    
listen = Anagram("listen")
print(listen.match(['enlists', 'google', 'inlets', 'banana']))
