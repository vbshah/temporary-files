import MySQLdb
from MySQLdb import escape_string as es
from vocabulary import Vocabulary as vb
import json


def convert(s):
    return es(s.encode('ascii', 'ignore').decode('ascii'))


def get_done_words():
    sql = "SELECT word FROM lexicon"
    cursor.execute(sql)
    results = cursor.fetchall()
    ls = [row[0] for row in results]
    return ls


def get_word_data(word):
    word = convert(word)
    sql = "SELECT * FROM lexicon WHERE word='%s'" % (word)
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        row = results[0]
        print "Your word '", row[1], "'"
        print "It's Meaning '", row[2], "'"
        print "It's Example '", row[3], "'"
    except Exception, e:
        print "Flag 0"
        print e


def get_example(word):
    try:
        examples = json.loads(vb.usage_example(word))
        example = ''
        limit = min(3, len(examples))
        for i in range(limit):
            example += examples[i]['text']+'...'    
        return example
    except Exception, e:
        print e,'\nFlag example'
        return ""


def get_meaning(word):
    try:
        meaning = json.loads(vb.meaning(word))
        means = ''
        limit = min(3, len(meaning))
        for i in range(limit):
            means += meaning[i]['text'] + ';'

        return means
    except Exception, e:
        print e
        return ""


def add_word(word, meaning1):
    if len(meaning1) != 0:
        meaning1 += ';'
    example = convert(get_example(word))
#    print "Example\n", example
    meaning2 = get_meaning(word)
    meaning = convert(meaning1 + meaning2)
    print "Meaning of", word, 'is'
    print meaning
    print "\nAnd Example"
    print example
    word = convert(word)
    sql = "INSERT INTO lexicon(word,meaning,example) VALUES ('%s' , '%s', '%s')" % \
        (word, meaning, example)
    try:
        cursor.execute(sql)
        db.commit()
        print "Word", word, "Added!"
    except Exception, e:
        print "Flag2"
        print e


def get_input():
    while 1:
        s = raw_input('Type word for input : ')
        if s in all_words:
            return s
        pass

try:
    db = MySQLdb.connect("localhost", "root", "", "GRE")  #your Password
    cursor = db.cursor()
    with open('words.txt') as f:
        all_words = set([i.strip() for i in f.readlines()])
except Exception, e:
    db.rollback()
    #    print "error", e


def main():

    done = set(get_done_words())
    while 1:
        try:
            word = get_input()
            if word == "exit":
                break
            else:
                if word in done:
                    print "You have already done this word"
                    get_word_data(word)
                else:
                    #                    meaning1 = raw_input("Type its meaning : ")
                    meaning1 = ''
                    done.add(word)
                    add_word(word, meaning1)
        except Exception, e:
            print "Flag3"
            print e

    print('Goodbye!')
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
