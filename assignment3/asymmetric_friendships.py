import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line
lista = []

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    friend = record[1]
    #words = value.split()
    #for w in words:
    mr.emit_intermediate((key, friend), 1)
    mr.emit_intermediate((friend, key), -1)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    total = 0
    for v in list_of_values:
      total += v

    if(total == 1):  
      mr.emit((key[0], key[1]))
      mr.emit((key[1], key[0]))  


    # if(total == -1):
    #   mr.emit((key[0], key[1]))
    #   mr.emit((key[1], key[0]))
    # if(total == 1):  
    #   mr.emit((key[0], key[1]))

    

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
