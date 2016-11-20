import operator

file=open("plik.txt","r+")
wordcount={}
for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
    
ordered = sorted(wordcount.items(), key=operator.itemgetter(1), reverse=True)
print(ordered)
