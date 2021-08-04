fileObject = open("USRE38691E1.txt", "r")
data = fileObject.read()
print(data)

# Python program to find the k most frequent words
# from data set
from collections import Counter
 
# split() returns list of all the words in the string
split_it = data.split()
  
# Pass the split_it list to instance of Counter class.
Counter = Counter(split_it)
  
# most_common() produces k frequently encountered
# input values and their respective counts.
most_occur = Counter.most_common(20)
  
print(most_occur)