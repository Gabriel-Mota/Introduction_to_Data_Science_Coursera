import sys
import json

def freq(tweet_file):
	dict_freq = {}

	count = 0
	for line in tweet_file:
		l = json.loads(line)
		if u'text' in l:
			text = l[u'text'].split()
			for word in text[2:]:
				count += 1
				#word = word.lower()
				if not(word in dict_freq):
					dict_freq[word] = 1
				else:
					dict_freq[word] += 1

	for word in dict_freq:
		print word + " " + str(dict_freq[word]/count)				





def main():
	tweet_file = open(sys.argv[1])
	freq(tweet_file)
	tweet_file.close()

if __name__ == '__main__':
    main()	