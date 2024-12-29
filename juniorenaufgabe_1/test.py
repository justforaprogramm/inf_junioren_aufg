from pprint import pprint
def find():
    area = 66/42
    inp = 23
    num_dict = {}
    search = []

    for x in range(inp, int(inp*1.1)+1):
        for num in range(1, x+1):
            num_dict.setdefault(x, []).append([num, ((num**2)/x) * area]) if x % num == 0 else ...

    for squares in num_dict:
        search.append([item[1] for item in num_dict[squares]])
    search = [value for sub in search for value in sub]

    perf_num = min(search, key=lambda x:abs(x-1))
    for squares in num_dict:
        for btmside in num_dict[squares]:
            if btmside[1] == perf_num:
                sqsq = squares
                bttt = btmside[0]
                break;
    lol = [5,6,7]
    print(lol[1])
    #print(f'there are {sqsq} squares with {bttt} felder by {int(sqsq/bttt)} in the square the size of {area}.')

def funktionier():
    lst = [0.06547619047619047, 0.26190476190476186, 0.5892857142857143, 1.0476190476190474, 2.357142857142857]

    print(min(lst, key=lambda x:abs(x-1)))

find()