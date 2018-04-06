sentence="Burk burku burk, brrrk, brk bark. Burczku Burk."
words=sentence.split()
#strip for multiple characters
words_after=[word.strip('.,') for word in sentence.split() if word != "Burk"]
#print(words_after)
#print(words)

##########################


liczby = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7, 0]

#liczby całkowite nieujemne z tablicy liczby
nowa = [int(liczba) for liczba in liczby if liczba >=0]

print(nowa)
