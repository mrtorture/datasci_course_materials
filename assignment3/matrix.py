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
    # key = record[0]
    # value = record[1]

    #print record[0], record[1], record[2], record[3]

    matrix = record[0]
    elementA = (matrix, record[2], record[3])
    elementB = (matrix, record[1], record[3])

    if matrix == 'a':
      for k in range(5):
        mr.emit_intermediate((record[1], k), record)
    if matrix == 'b':
      for i in range(5):
        mr.emit_intermediate((i, record[2]), record)

    #words = value.split()
    #for w in words:
    

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    
    A = []
    B = []

    for value in list_of_values:
      if value[0] == 'a':
        A.append((value[1], value[2], value[3]))
      if value[0] == 'b':
        B.append((value[1], value[2], value[3]))

    t = 0
    for a in A:
      for b in B:
        if a[0] == key[0] and b[1] == key[1]  and a[1] == b[0]: 
          s = a[2] * b[2]
          t += s

    #print key, t
    

    mr.emit((key[0], key[1], t))


    # A = []
    # B = []

    # mij = []
    # njk = []

    # for value in list_of_values:
    #   if value[0] == 'a':
    #     A.append((value[1], value[2], value[3]))
    #   if value[0] == 'b':
    #     B.append((value[1], value[2], value[3]))

    # for value in A:
    #   if value[0] == key[0]:
    #     print value
    #     mij.append(value[2])
    # for value in B:
    #   if value[1] == key[1]:
    #     print value
    #     njk.append(value[2])

    # print mij, njk


      

      #print len(value)

      #print value
    #print key 
      #mr.emit((key, )

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
