import docx
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import wordnet
import codecs

ps = PorterStemmer()

with open("hardwords.txt", "r") as f:
    hardwords = [str(i).rstrip() for i in f.readlines()]

def meaning(word):
    try:
        if word in hardwords:
            syns = wordnet.synsets(word)
            print("done")
            return word + "[[" + syns[0].definition() + "]]"
        else:
            return word
    except:
        print("error for word", word)
        return word
    return "vbshah"
with open("breaker.txt", "r") as f:
    breaker = f.read()

print("testing to find meaning")
try:
    print("word is ",hardwords[14])
    syns=wordnet.synsets(hardwords[14])
    print("meaning ",syns[0].defination())
except:
    print("not found!!")
with codecs.open("output", "r", 'utf-8') as f:
    ls = f.read().split(breaker)
#    print("len", len(ls))
# print("this is working fast now !!!! .........or so i hope")
doc = docx.Document()
para = ls[10]
lines = para.split('\n')
with codecs.open("second.txt", "wb", 'utf-8') as f:
    for i in lines:
        try:
            tmp = [meaning(str(i).lower()) for i in word_tokenize(i)]
#           print("word",tmp)
            doc.add_paragraph(' '.join(tmp))
            f.write(' '.join(tmp) + "\n")
        except:
            #            print("we missed", i)
            pass

doc.save("tmp1.docx")
