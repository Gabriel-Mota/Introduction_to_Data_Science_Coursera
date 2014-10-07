import sys
import json
import operator


def sentiment(tweet_file):
	afinnfile = open(sys.argv[1])
	scores = {} # initialize an empty dictionary
	states = {}
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
	 		if u'place' in l and l[u'place'] is not None:
	 			place = l[u'place']
	 			location = l[u'user']
	 			if u'country' in place:
	 				# print place[u'country']
		 			#if place[u'country'] == "United States":
	 				if u'full_name' in place:
	 					# if location[u'lang'] == "en":
	 					aux3 = place[u'full_name'].split()
	 					if(len(aux3)>1):
	 						if(len(aux3[1]) == 2):		
			 					name = aux3[1]
			 					text = l[u'text'].split()
								for word in text:
									if word in scores:
					 					score += scores[word]
								if not(name in states):
									states[name] = score
								else:
									states[name] += score

	happiest = sorted(states.iteritems(), key=operator.itemgetter(1), reverse = True)								
	#happiest = max(states.iteritems(), key=operator.itemgetter(1))[0]							
	if(len(happiest)>0):
		print happiest[0][0]

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
