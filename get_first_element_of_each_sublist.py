#  extract first element of each sublist in the given list of lists.
# Input = [[1,2],[3,4,5],[6,7,8,9]]
# Output = [1,3,6]

def process():
    list = [[1,2],[3,4,5],['x',7,8,9]]
    out = []

    for x in list:
        for x1 in x:
            out.append(x1)
            break
    print(out)


if __name__ == '__main__':
    process()
