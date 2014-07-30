import MapReduce
import sys

"""
Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    value = record[1]
    order = []
    lineitem = []

    for item in range(len(record)):
          order.append(record[item])


    mr.emit_intermediate(value, record)

def reducer(key, list_of_values):

    #print key, list_of_values[1]
    # key: word
    # value: list of occurrence counts
    order = []
    item = []

    #print list_of_values
    
    for value in list_of_values:
      if value[0] == 'order':
        order.append(value)
      if value[0] == 'line_item':
        item.append(value)
    
    for o in order:
        for i in item:
            mr.emit(o+i)

    #  if v[0] == 'order':
        #print v, list_of_values[1]

    #print len(total)

    #mr.emit((key, order+item))

    #print len(list_of_values)
    #print total

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
