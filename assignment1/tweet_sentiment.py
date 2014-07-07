import sys
import json

scores = {}


def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def jsonr(line):
	return json.loads(line)

def toLines(file):
	tweet_lines = []

	for line in file:
		tweet_lines.append(jsonr(line))

	return tweet_lines

def calculateEmotion(tweet):
	word_score = 0
	sliced_tweet = tweet["text"].split()
	for word in sliced_tweet:
		for term in scores:
			if word == term:
				word_score += scores[term]
	return word_score


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    for line in sent_file:
    		term, score = line.split("\t")
    		scores[term] = int(score)

    #hw()
    #lines(sent_file)
    #lines(tweet_file)

    array_of_lines = toLines(tweet_file)

    #print array_of_lines[10]["text"].split()
    for lines in range(len(array_of_lines)):
    	if "text" in array_of_lines[lines]:
    		print calculateEmotion(array_of_lines[lines])

if __name__ == '__main__':
    main()
