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
        sliced_tweet.append(word.translate(None, ' [!@$:\',./\_;%"(?)*').lower())
    return sliced_tweet

def frequency(text):
    times = {}
    freq = []
    counter = 0

    for line in range(len(text)):
        if "entities" in text[line]:
            if "hashtags" in text[line]["entities"]:
                    if text[line]["entities"]["hashtags"]:
                        hashtag = text[line]["entities"]["hashtags"][0]["text"]
                        #print hashtag
                        if hashtag not in times:
                            times[hashtag] = 1
                            #print hashtag
                        else:
                            times[hashtag] += 1
    #        sliced_tweet = sliceTweet(text[line]["text"])

            #for word in sliced_tweet:
            #    counter += 1

            #    if '#' in word:
                    #print word

            #        if word not in times and word != ' ':
            #            times[word] = 1
                
            #        else:
            #            times[word] += 1

    sort = sorted(times, key=times.get, reverse=True)[:10]

    for word in sort:
        print word, float(times[word])
                #print freq[str(item[0])]

    #return freq


def main():
    tweet_file = open(sys.argv[1])

    array_of_lines = toLines(tweet_file)

    frequency(array_of_lines)

if __name__ == '__main__':
    main()
