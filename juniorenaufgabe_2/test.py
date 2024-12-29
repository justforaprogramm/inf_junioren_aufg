import functools
import string
#used_low = 'WoW'

#print(len(used_low.lower().strip()))

#print(ord('a') -96) #The ord() function returns the number representing the unicode code of a specified character.

# input  = ' c fff'
# inputl = len(input)
# start0 = [0, 0]
# start1 = [0, 1]
# temp_num = 0

# print(f'{start0},{start1}')

# @functools.cache
# def ording(str,index) -> int:
#     if str[index].lower() in string.ascii_lowercase:
#         return ord(str[index].lower()) -96
#     return index
    


# while start0[1] < inputl:
#     temp_num = start0[1]
#     start0[1] += ording(input, start0[1])
#     if temp_num == start0[1]:
#         start0[1] += 1 
#     else:
#         start0[0] += 1

# while start1[1] < inputl:
#     temp_num = start1[1]
#     start1[1] += ording(input, start1[1])
#     if temp_num == start1[1]:
#         start1[1] += 1 
#     else:
#         start1[0] += 1


# print(f'{start0},{start1}')