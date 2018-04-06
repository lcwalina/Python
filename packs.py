import re

array = (dir(re))

#Listy składane (!!!)
#http://www.secnetix.de/olli/Python/list_comprehensions.hawk
matchings = [match for match in array if "find" in match]

#alphabetical sort
matchings.sort()

#reversed sort
matchings.sort(reverse=True)
print(matchings)
