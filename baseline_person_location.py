import urllib2
from bs4 import BeautifulSoup
import nltk
import matplotlib
import matplotlib.pyplot as plt
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.sem import relextract
import re
from nltk.sem.relextract import extract_rels, rtuple
from collections import Counter
from PIL import Image

# with open('sherlock.txt', 'r') as f:
#     sample = f.read().decode('utf-8')
#     sample = sample.encode('ascii', 'ignore')




stop_words = set(stopwords.words('english'))

def interaction(document):
    dictionary ={}
    noun = []
    noun_text = []
    document = ' '.join([i for i in document.split() if i not in stop_words])
    sentences_orig = nltk.sent_tokenize(document)
    sentences_token = [nltk.word_tokenize(sent) for sent in sentences_orig]
    sentences = [nltk.pos_tag(sent) for sent in sentences_token]
    # for s in sentences:
    #     for sent in sentences_token:
    #       tag = sent[1]
    #       if tag == 'NN':
    #         noun_text.append(tag)
    grammar = "NP:{<NN><V.*><NN>}"

    cp = nltk.RegexpParser(grammar)
    for s in sentences:
      noun.append(cp.parse(s))
    for sent in document:
        sentences_orig = nltk.sent_tokenize(document)
        for s in sentences_orig:
         for chunk in nltk.ne_chunk(sentences_orig):
          if type(chunk) == nltk.tree.Tree:
              if chunk.label() == 'PERSON' or chunk.label == 'LOCATION':
               noun_text.append(''.join([s[0] for s in sentences_orig]))
    return noun_text
#
#
def ie_preprocess(document):
    document = ' '.join([i for i in document.split() if i not in stop_words])
    sentences = nltk.sent_tokenize(document)
    sentences = [nltk.word_tokenize(sent) for sent in sentences]
    sentences = [nltk.pos_tag(sent) for sent in sentences]
    #chunked_sentences = nltk.batch_ne_chunk(sentences)
    return sentences

def extract_names(document):
    names = []
    per_sentence =[]
    sentences = ie_preprocess(document)
    for tagged_sentence in sentences:
        for chunk in nltk.ne_chunk(tagged_sentence):
            if type(chunk) == nltk.tree.Tree:
                if chunk.label() == 'PERSON':
                    names.append(' '.join([c[0] for c in chunk]))
    count = Counter(names)
    count_names = count.most_common(10)
    count_names = dict(count_names)

    return count_names

def extract_location(document):
    location = []
    sentences = ie_preprocess(document)
    for tagged_sentence in sentences:
        for chunk in nltk.ne_chunk(tagged_sentence):
            if type(chunk) == nltk.tree.Tree:
                if chunk.label() == 'LOCATION':
                    location.append(' '.join([c[0] for c in chunk]))
    count_location = dict(Counter(location))
    return count_location





if __name__ == '__main__':


    url = "http://www.gutenberg.org/cache/epub/103/pg103.txt"
    html = urllib2.urlopen(url).read().decode('utf8')
    raw = BeautifulSoup(html, 'html.parser').get_text()
    sample = raw.encode('ascii', 'ignore')

    names = extract_names(sample)
    location = extract_location(sample)
    plt.figure(1)

    # print names
    # print location
    # nn = interaction(sample)
    # print nn
    plt.figure(1)
    plt.xlabel('Locations in the book')
    plt.ylabel('no. of times characters visited location')
    plt.bar(range(len(location)), location.values(), align='center')
    # plt.margins(0.2)
    plt.xticks(range(len(location)), location.keys(), rotation = 20)
    plt.savefig('location_graph.png')
    # plt.show()

    plt.figure(2)
    plt.xlabel('Characters in the book')
    plt.ylabel('no. of times characters visited loaction')
    plt.bar(range(len(names)), names.values(), align='center')
    plt.xticks(range(len(names)), names.keys(), rotation = 20)
    plt.savefig('names_graph.png')

    # plt.show()

