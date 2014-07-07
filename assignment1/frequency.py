import sys
import json

scores = {}
hardcore = {}


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


def sliceTweet(non_formated_tweet):
    sliced_tweet = []
    encoded_tweet = non_formated_tweet.encode('utf-8').split()
    for word in encoded_tweet:
        sliced_tweet.append(word.translate(None, ' [!@#$:\',./\_;%"(?)*').lower())
    return sliced_tweet

def frequency(text):
    times = {}
    freq = {}
    counter = 0

    for line in range(len(text)):
        if "text" in text[line]:
            sliced_tweet = sliceTweet(text[line]["text"])

            for word in sliced_tweet:
                counter += 1

                if word not in times and word != ' ':
                    times[word] = 1
                
                else:
                    times[word] += 1

            for item in times.items():
                print str(item[0]), float(times[item[0]])/float(counter)
                #print freq[str(item[0])]

    #return freq


def main():
    tweet_file = open(sys.argv[1])

    array_of_lines = toLines(tweet_file)

    frequency(array_of_lines)

if __name__ == '__main__':
    main()
