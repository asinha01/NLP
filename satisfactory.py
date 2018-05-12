import os
from bs4 import BeautifulSoup
import urllib2
import nltk

# class Agent:
# dire = os.getcwd()
# listOfdir = os.listdir(dire)
# while True:


    # UserFileName = raw_input("Enter filename:")
    # if (UserFileName in listOfdir) and (UserFileName.endswith('.txt')):
    #     InputFile = open(UserFileName,'r')
    #     text = InputFile.read()
def fres_score(doc):
        text = doc
        sentence = text.count(".") + text.count('!') + text.count(";") + text.count(":") +text.count("?")

        words = len(text.split())
        syllable = 0

        for word in text.split():
            for vowel in ['a','e','i','o','u']:
                syllable += word.count(vowel)
                for ending in ['es', 'ed', 'e']:
                    if word.endswith(ending):
                        syllable -= 1
                    if word.endswith('le'):
                        syllable += 1

        G = round((0.39 * words) / sentence + (11.8 * syllable) / words - 15.59)

        print "Fres score is \t:-", G


        print 'This text has % d words' % (words)
        if G >= -5 and G <= 30:
            print 'The Readability level is College'
        elif G >= 50 and G <= 60:
            print 'The Readability level is High School'
        elif G >= 90 and G <= 100:
            print 'The Readability level is fourth grade'

        return G

    # elif UserFileName not in listOfdir:
    #     print "This text file does not exist in current directory"
    # elif not(UserFileName.endswith('.txt')):
    #        print "This is not a text file."

# class Environment():
#     def data(self):
#      url = "http://www.gutenberg.org/files/2554/2554-0.txt"
#      html = urllib2.urlopen(url).read().decode('utf8')
#      raw = BeautifulSoup(html).get_text()
#      raw = raw.encode('ascii', 'ignore')
#
#
#      #print raw
#      return raw

def main():
    url = "http://www.gutenberg.org/files/2554/2554-0.txt"
    html = urllib2.urlopen(url).read().decode('utf8')
    raw = BeautifulSoup(html,'html.parser').get_text()
    raw = raw.encode('ascii', 'ignore')
 # e = Environment()
 # doc = e.data()
 # a = Agent()
    G = fres_score(raw)
    if G >= 0 and G <= 30:
     print "Fres score", G
     print 'The Readability level is College'
    elif G >= 50 and G <= 60:
      print "Fres score", G
      print 'The Readability level is High School'
    elif G >= 90 and G <= 100:
     print "Fres score", G
     print 'The Readability level is fourth grade'

main()