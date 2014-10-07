import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))



def sentiment(tweet_file):
	afinnfile = open(sys.argv[1])
	scores = {} # initialize an empty dictionary
	for line in afinnfile:
	  term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
	  scores[term] = int(score)  # Convert the score to an integer.

	#count = 0
	for line in tweet_file:
		score = 0 
		#if count > 10:
		#	break
		#else:	
		l = json.loads(line)
		if u'text' in l:
			text = l[u'text'].split()
			for word in text:
				if word in scores:
					score += scores[word]	
		#count +=1
		print score
	afinnfile.close()				


def main():
    #sent_file = open(sys.argv[1], "rw+")
    tweet_file = open(sys.argv[2])
    #hw()
    #lines(sent_file)
    sentiment(tweet_file)
    tweet_file.close()
 
    #tweet_file = open(sys.argv[2], "rw+")   
    #lines(tweet_file)
    #tweet_file.close()
    #sent_file.close()
    


if __name__ == '__main__':
    main()
