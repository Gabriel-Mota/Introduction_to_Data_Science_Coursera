import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def sentiment(text, scores):
	score = 0
	for word in text:
		if word in scores:
			score += scores[word]
	return score		

def term(tweet_file):
	afinnfile = open(sys.argv[1])
	scores = {} # initialize an empty dictionary
	for line in afinnfile:
	  term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
	  scores[term] = int(score)
	#scores2 = scores.copy()
	scores2 = {}  

	for line in tweet_file:
		l = json.loads(line)
		if u'text' in l:
			text = l[u'text'].split()
			for word in text[2:]:
				word = word.lower()
				if not(word in scores):
					if not(word in scores2):
						scores2[word] = 0
					scores2[word] += sentiment(text, scores)			
					

	for word in scores2:
		print word + " " + str(scores2[word])

	afinnfile.close()					


def main():
    #sent_file = open(sys.argv[1])
    #afinnfile = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #hw()
    #lines(sent_file)
    #lines(tweet_file)
    term(tweet_file)

    


   #  scores = {}
   #  for line in afinnfile:
	  # term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
	  # scores[term] = int(score)


    #text = [u'RT', u'@reversezarry:', u'Theo:', u'"how', u'old', u'r', u'u?"', u'Me:', u'"18"', u'Theo:', u'"ur', u'too', u'old"', u'Me:', u'"18', u'minus', u'17', u'you', u"didn't", u'let', u'me', u'finish"']
    #print sentiment(text, scores)
    #sent_file.close()
    #afinnfile.close()
    tweet_file.close()


if __name__ == '__main__':
    main()
