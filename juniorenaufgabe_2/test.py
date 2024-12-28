import functools
used_low = 'WoW'

#print(len(used_low.lower().strip()))

#print(ord('a') -96) #The ord() function returns the number representing the unicode code of a specified character.

input  = 'bol'
inputl = len(input)
start0 = [0, 0]
start1 = [0, 1]


print(f'{start0},{start1}')

@functools.cache
def ording(str,index) -> int:
    return ord(str[index]) -96

while start0[1] < inputl:
    start0[1] += ording(input, start0[1])
    start0[0] += 1

while start1[1] < inputl:
    start1[1] += ording(input, start1[1])
    start1[0] += 1


print(f'{start0},{start1}')