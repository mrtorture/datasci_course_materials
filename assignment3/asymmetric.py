import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    #print record
    #words = record.split()
    #for w in words:
    #print words
    #print key, value
    person = record[0]
    friend = record[1]

    mr.emit_intermediate((person, friend), 1)
    mr.emit_intermediate((friend, person), -1)
    #print friendship

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    #total = []
    total = 0
    for v in list_of_values:
      total += v

    if total != 0:
      mr.emit((key))


    #for name in list_of_values:
    #  mr.emit((key, name))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
