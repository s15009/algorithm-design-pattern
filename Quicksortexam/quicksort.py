#!/usr/bin/python3
LOOP_COUNT = 5000
LIST_COUNT = 1000
MAX_NUM = 10000


def data_generate():
    import random
    return [random.randint(1, MAX_NUM) for _ in range(LIST_COUNT)]


def quick_sort(data):
    if len(data) < 1:
        return data
    pivot = data[0]
    left = []
    right = []
    for x in range(1,len(data)):
        if data[x] <= pivot:
            left.append(data[x])
        else:
            right.append(data[x])
    left = quick_sort(left)
    right = quick_sort(right)
    
    return left + [pivot] + right

def quick_sort2nd(data):
    #counter = 0
    #挿入ソートに切り替える
    if len(data) <= 64:
        return insertion_sort(data)
    pivot = data[0]
    #配列の２つを比べて小さい方を基準にする
    #if len(data) > 2:
        #pivot = data[1] if data[1] < data[0]  else data[0]
    #CENTER = data[(len(data) // 2):(len(data) // 2+1)]
    #center = data[0] + data[-1] / 2
    #if (counter >= 2):
        #counter += 1
        #if len(data) > 2:
            #pivot = data[1] if data[1] < data[0]  else data[0]
        #if len(data) > 4:
            #pivot = data[0] if data[0] < data[-1] else data[-1]
            #pivot = center if center < pivot else pivot
    left = []
    right = []
    for x in range(1,len(data)):
        if data[x] <= pivot:
            left.append(data[x])
        else:
            right.append(data[x])

    left = quick_sort(left)
    right = quick_sort(right)

    return left + [pivot] + right

def insertion_sort(data):
    for i in range(1, len(data)):
        tmp = data[i]
        if data[i-1] > tmp:
            j = i
            while j > 0 and data[j-1] > tmp:
                data[j] = data[j-1]
                j -= 1
            data [j] = tmp


if __name__ == '__main__':
    import time
    import sys

    start = time.time()
    for _ in range(10000):
        data = data_generate()
        quick_sort(data)
        #[print(',', end='' ) if _ % 100 != 99 else print(int(_ / 100 + 1))]
        sys.stdout.flush()
    end = time.time()
    print('初期クイックソート')
    print('経過時間、', (end-start))
    print('平均時間、', ((end-start) / 10000))



    #data = data_generate()
    #a = quick_sort2nd(data)
    #print(a)
    start = time.time()
    for _ in range(10000):
        data = data_generate()
        quick_sort2nd(data)
        #[print(',', end='' ) if _ % 100 != 99 else print(int(_ / 100 + 1))]
        sys.stdout.flush()
    end = time.time()
    print('クイックソート2nd')
    print('経過時間、', (end-start))
    print('平均時間、', ((end-start) / 10000))

