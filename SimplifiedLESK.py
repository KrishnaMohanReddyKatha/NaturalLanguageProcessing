""" Author: Krishna Mohan Reddy Katha
    Net Id : KXK171830
    Simplified LESK Algorithm """

from nltk.corpus import wordnet
from nltk.corpus.reader import NOUN
from nltk.corpus import stopwords


def LESK(word, sentence):
    syns = wordnet.synsets(word, NOUN)
    bestSense = syns[0]
    maxOverlap = 0
    result = {}
    sentenceWords = sentence.split()
    sentenceWords = removeStopWords(sentenceWords)
    sentenceWords = list(set(sentenceWords))
    sentenceWords.remove("bank")
    for sense in syns:
        senseComparator = sense.definition().split()
        exs = sense.examples()
        for ex in exs:
            senseComparator+= ex.split()
        senseComparator = removeStopWords(senseComparator)
        senseComparator = list(set(senseComparator))
        if "bank" in senseComparator:
            senseComparator.remove("bank")
        overlap, overlapWords = computeOverlapCount(senseComparator, sentenceWords)
        result[sense] = (overlap, overlapWords)
        if overlap > maxOverlap:
            maxOverlap = overlap
            bestSense = sense
    return (bestSense, maxOverlap, result)

def removeStopWords(words):
    stop = []
    stop = stopwords.words('english')
    return [word for word in words if word not in stop]

def computeOverlapCount(corpusWords, sentenceWords):
    overlapWords = []
    overlapCount = 0
    for item in sentenceWords:
        count = corpusWords.count(item)
        if (count > 0):
            overlapWords.append(item)
            overlapCount += 1
    return overlapCount, overlapWords



if __name__ == "__main__" :
 sentence = "The bank can guarantee deposits will eventually cover future tuition costs because it invests in adjustable-rate mortgage securities"
 word = "bank"


 bstSense, maxOverlap, overlaps = LESK(word, sentence)

 print "Sentence : " + sentence
 print "Chosen Word : " + word
 print "Default POS Chosen : NOUN"

 print '{:^40}'.format("Sense"), '{:^40}'.format("Overlap Count")
 for sense in overlaps:
    print '{:^40}'.format(sense.name()), '{:^40}'.format(overlaps[sense][0])

 print "\n"
 print "Best Sense\t: ", bstSense.name()
 print "Total Overlaps\t: ", overlaps[bstSense][0]
