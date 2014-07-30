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
    identifier = record[0]
    full_sequence = record[1]
    
    #print identifier, full_sequence

    short_sequence = full_sequence[:-10]

    #print len(full_sequence), len(short_sequence)
    
    #for w in words:
    mr.emit_intermediate(short_sequence, 1)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    #total = 0
    #for v in list_of_values:
    #  total += v

    mr.emit(key)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
