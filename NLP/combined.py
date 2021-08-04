filenames = ['RE30525',
 'RE30135',
 'RE29872',
 'RE30334',
 'RE30120',
 'RE29993',
 'RE30440',
 'RE30423',
 'RE30981',
 'RE30932',
 'RE31296',
 'RE31154',
 'RE31196',
 'RE32125',
 'RE31627',
 'RE31361',
 'RE31451',
 'RE31956',
 'RE31713',
 'RE32175',
 'RE32546',
 'RE32433',
 'RE33058',
 'RE33126',
 'RE33551',
 'RE33950',
 'RE34064',
 'RE34023',
 'RE34260',
 'RE34493',
 'RE34146',
 'RE34142',
 'RE34359',
 'RE34565',
 'RE35425',
 'RE39487',
 'RE38691',
 'RE39327',
 'RE36722',
 'RE38615',
 'RE37731',
 'RE42607',
 'RE44839',
 'RE39757',
 'RE42767',
 'RE39598',
 'RE39669',
 'RE39440',
 'RE40615',
 'RE43074']

filenamestxts = [file + ".txt" for file in filenames]

print(filenamestxts)

# Open file3 in write mode
with open('combined.txt', 'w') as outfile:
  
    # Iterate through list
    for names in filenamestxts:
  
        # Open each file in read mode
        with open(names) as infile:
            # read the data from file1 and
            # file2 and write it in combined.txt
            outfile.write(infile.read())
        # Add '\n' to enter data of file2
        # from next line
        outfile.write("\n")

fileObject = open("combined.txt", "r")
data = fileObject.read()
# print(data)

# Python program to find the k most frequent words
# from data set
from collections import Counter
# split() returns list of all the words in the string
split_it = data.split()
# Pass the split_it list to instance of Counter class.
Counter = Counter(split_it)
# most_common() produces k frequently encountered
# input values and their respective counts.
most_occur = Counter.most_common(50)
print(most_occur)

for item in most_occur:
    print(item)