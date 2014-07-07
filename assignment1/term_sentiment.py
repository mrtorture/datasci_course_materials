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

def calculateEmotion(sliced_tweet):
	word_score = 0
	for word in sliced_tweet:
		if word in scores:
			word_score += scores[word]
	return word_score

def sliceTweet(non_formated_tweet):
    sliced_tweet = []
    encoded_tweet = non_formated_tweet.encode('utf-8').split()
    for word in encoded_tweet:
        sliced_tweet.append(word.translate(None, ' !@#$:\',./\_;%"(?)').lower())
    return sliced_tweet

def calculateTweetEmotion(sliced_tweet):
    word_score = 0
    for word in sliced_tweet:
        if word in hardcore:
            #print word, hardcore[word]
            word_score += hardcore[word]
        if word in scores:
            word_score += scores[word]
    return word_score

def nonMatchingWords(text):
    non_sentiment_words = {}

    for line in range(len(text)):
        if "text" in text[line]:
            sliced_tweet = sliceTweet(text[line]["text"])

            for word in sliced_tweet:
                if word not in scores and word != ' ':
                    tweet_score = calculateEmotion(sliced_tweet)
                    #print word, tweet_score
                    if word in non_sentiment_words:
                        non_sentiment_words[str(word)][2]+=1
                        #print word, non_sentiment_words[str(word)]

                        if tweet_score > 0:
                            non_sentiment_words[str(word)][0]+=1
                        else:
                            non_sentiment_words[str(word)][1]+=1

                    else:
                        if tweet_score > 0:
                            non_sentiment_words[str(word)] = [1,0,1]
                        else:
                            non_sentiment_words[str(word)] = [0,1,1]
 
    return non_sentiment_words

def grades(non_scored_words):
    #print non_scored_words
    for word in non_scored_words.items():

        #print word

        a = float(non_scored_words[word[0]][0])
        b = float(non_scored_words[word[0]][1])
        c = float(non_scored_words[word[0]][2])

        if b/c != 0:
            #grades[str(word[0])] == 
            #print word[0],a,b,c, #,a/c, ((a/c)/(b/c))
            hardcore[str(word[0])] = ((a/c)/(b/c))
        if b/c == 0:
            hardcore[str(word[0])] = (a)
       

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
    grades(nonMatchingWords(array_of_lines))
    
    #for item in hardcore.items():
        #print item

    #print array_of_lines[10]["text"].split()
    #teste = "Hi, I love happy mufasas black death."
    #print calculateTweetEmotion(sliceTweet(teste))

    #counter(nonMatchingWords(array_of_lines))

    for lines in range(len(array_of_lines)):
    	if "text" in array_of_lines[lines]:
            sliced_tweet = sliceTweet(array_of_lines[lines]["text"])
            #print sliced_tweet
            for word in sliced_tweet:
                if word in hardcore:
                    #None
                    print word, hardcore[word]
                if word in scores:
                #    None
                    print word, scores[word]
                #if word not in hardcore and word not in scores:
                #    print word

if __name__ == '__main__':
    main()
