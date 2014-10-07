import sys
import json
import operator


def hashs(tweet_file):
	tags = {}
	for line in tweet_file:
	    	l = json.loads(line)
	    	if u'text' in l:
				ent = l[u'entities']
				hashs = ent[u'hashtags']
				for tag in hashs:
					text = tag[u'text']
					if not(text in tags):
						tags[text] = 1
					else:
						tags[text] += 1


	# for i in tags:
	# 	print i + " " + str(..)
	sorted_x = sorted(tags.iteritems(), key=operator.itemgetter(1), reverse = True)

	for item in sorted_x[0:10]:
		print item[0] + " " + str(item[1])					


def main():
    tweet_file = open(sys.argv[1])
    hashs(tweet_file)

    tweet_file.close()


if __name__ == '__main__':
    main()				