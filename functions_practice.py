def hello():
    print('Hello!')

hello()

def pack(item1, item2, item3):
    return [item1, item2, item3]

lunchbox = pack('banana', 'candy', 'water')
print(lunchbox)

def eat_lunch(list):
    #edge case first
    if not list:
        print('My lunchbox is empty!')
    else:
        print(f"First I eat a {list[0]}")
        for i in range(1, len(list)):
            print(f"Next I eat {list[i]}")

eat_lunch(lunchbox)

