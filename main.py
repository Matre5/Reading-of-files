# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from itertools import count
from posixpath import split
import re


def read_file_content(filename):
    # [assignment] Add your code here 
    #openfile = open("./story.txt", "r")
    
    with open("./story.txt" ,"r") as filee:
        
      read_file_content = filee.read()
      #print(read_file_content)
      print("Read the file\n")
      
    return read_file_content

def count_words():

    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    spliting_the_text = text.split()
    #print(text)
    #print(spliting_the_text)
    table_of_words ={}  #this is a dictionary of words
    for i in spliting_the_text:
        if i in table_of_words:
            table_of_words[i] +=1
        else:
            table_of_words[i] =1
    return table_of_words

print(count_words())
    
        
    



