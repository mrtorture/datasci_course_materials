import sys
import json

scores = {}
hapiness = {}

states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}


def lines(fp):
    print str(len(fp.readlines()))

def jsonr(line):
	return json.loads(line)

def toLines(file):
	tweet_lines = []

	for line in file:
		tweet_lines.append(jsonr(line))

	return tweet_lines

def sliceState(non_formated_state):
    sliced_state = []
    encoded_tweet = non_formated_state.encode('utf-8').split(', ')
    for word in encoded_tweet:
        sliced_state.append(word.translate(None, '!@#$:\',./\_;%"(?)'))
    return sliced_state

def sliceTweet(non_formated_tweet):
    sliced_tweet = []
    encoded_tweet = non_formated_tweet.encode('utf-8').split()
    for word in encoded_tweet:
        sliced_tweet.append(word.translate(None, ' !@#$:\',./\_;%"(?)').lower())
    return sliced_tweet

def calculateEmotion(sliced_tweet):
    word_score = 0
    for word in sliced_tweet:
        if word in scores:
            word_score += scores[word]
    return word_score

def happiestState(text):
    tweet_by_place = {}

    for line in range(len(text)):
        if "place" in text[line]:
            if text[line]["place"] is not None:
                if text[line]["place"]["country"] == "United States":
                    places = sliceState(text[line]["place"]["full_name"])
                    tweet_emotion = calculateEmotion(sliceTweet(text[line]["text"]))

                    if places[1] in states:
                        hapiness[places[1]] = tweet_emotion
                        #print places[1], tweet_emotion
                    else:
                        for abv, state in states.items():
                            if state == places[0]:
                                hapiness[abv] = tweet_emotion
                                #print abv + "  HAHA"
    print max(hapiness, key=hapiness.get)

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

    happiestState(array_of_lines)

    #print array_of_lines[8]["coordinates"]#.split()
    #for lines in range(len(array_of_lines)):
    #	if "text" in array_of_lines[lines]:
    #		print calculateEmotion(array_of_lines[lines])

if __name__ == '__main__':
    main()
