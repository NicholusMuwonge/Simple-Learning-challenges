from itertools import groupby

some=['eat', 'em','tea', 'lump', 'me', 'plum']

annogramed=[list(arranged) for  words,arranged in groupby(sorted(some, key=sorted),sorted)]

print (annogramed)
