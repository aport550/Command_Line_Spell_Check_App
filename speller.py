import sys

#takes in file from user
user_file = sys.argv[-1]

def speller(file):
    
    # create an empty list later to be used as the dictionary
    dict = []
    
    #fill our dict list with all the words from our dictionary file, all lowercased and endlines removed for formatting
    with open('wordlist.txt') as f:
        for word in f:
            word = word[:-1]
            word = word.lower()
            dict.append(word)
            
    #add these to dict so they dont come up as mispelled
    endlines = ["\n", "\t", '', "\n\n" , "\n\n\n"]
    symbols = [".", "...", "?", "!", "-", "_", "+", "=", "(", ")", "[", "]", ";", ":"]

    for line in endlines:
        dict.append(line)
    for symbol in symbols:
        dict.append(symbol)
    
    #create a list for the words in the file user uploaded
    words_list = []

    #place all the user file words into a list so they can be later compared with the dictionary list
    with open(file) as g:
        g =  g.read()
        line = g.split(" ")

    #check for capitals so we can check if base word is misspelled
    for l in line:
        if l.istitle():
            lower_case = l.lower()
            if lower_case in dict:
                dict.append(l)
            else:
                pass
        words_list.append(l)

    #check if words contain symbols or endlines if so check if their base word is spelled correctly
    for w in words_list:
        char_count = 0
        base_word = "zxzxxxxx"
        for char in w:
            if char in symbols or char in endlines:
                base_word = w[:-char_count]
                char_count = char_count + 1
            else:
                char_count = char_count + 1
        if base_word in dict:
            dict.append(w)
        else:
            pass

    # Compare our user word list to the dictionary word list and see which words match and are spelled correctly
    print("\nYour file was checked succesfully! Below is the content of your file with mispelled words indicated by a (Mispelled) added onto them.\n")
          
    for n in words_list:
        if n in dict:
             print(n + " ", end='')
        else:
            print(n+"(Mispelled) ", end=''), #mispelled words are denoted as having (Mispelled) added after them

    print('\n')
    return words_list;

speller(user_file)
