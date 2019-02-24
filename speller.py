import sys

#takes in file from user
user_file = sys.argv[-1]

def speller(file):
    
    # create a list for the wordlist
    dict = []
    
    #add all the words from our dictionary into the dictionary list with their correct formats
    with open('wordlist.txt') as f:
        for word in f:
            word = word[:-1]
            word = word.lower()
            dict.append(word)

    #create a list for the input words
    words_list = []

    #place all the input words into a list so they can be compared with the dictionary list
    with open(file) as g:
        g = g.read()
        line = g.split(" ")

    #check for capitals
    capital_words = []
    for l in line:
        first_char = (l[0])
        if first_char.isupper():
            l = l.lower()
            capital_words.append(l)
        words_list.append(l)

    #check for periods
    count = 0
    lwos = []

    for w in words_list:
        if w[len(w)-1] == ".":
            this_word = words_list[count]
            words_list[count] = this_word[:-1]
            lwos.append(words_list[count])
            count = count+1
        else:
            count = count+1

#compare word list to dict list and see if there are words from words list that aren't in dict list if so mark as mispelled

    def neither_in(a, b, c):
        d = b+c
        if(a not in d):
            return True
        else:
            return False

    for n in words_list:
        if n in dict:
            if neither_in(n, lwos, capital_words):
                print(n),
            if(n in capital_words):
                n = n.capitalize()
                print(n),
            if(n in lwos):
                print(n+"."),
        else:
            print(n+"(Mispelled)"),
    return words_list;

speller(user_file)
