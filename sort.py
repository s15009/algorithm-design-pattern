#!/usr/bin/python3
LOOP_COUNT = 5000
LIST_COUNT = 1000
MAX_NUM = 10000

def data_generate():
    import random
    return [random.randint(1, MAX_NUM) for _ in range(LIST_COUNT)]

def selection_sort(data):
    for i in range(len(data) - 1):
        minimum = i
        
        for t in range(i + 1, len(data)):
            if data[minimum] > data[t]:
                minimum = t

        data[i], data[minimum] = data[minimum], data[i]

def bubble_sort(data):
    for i in range(len(data)):
        for t in range(1, len(data) - i):
                if data[t] < data[t-1]:
                    data[t], data[t-1] = data[t-1], data[t]


def insertion_sort(data):
    for i in range(1, len(data)):
            tmp = data[i]
            if data[i-1] > tmp:
                j = i
                while j > 0 and data[j-1] > tmp:
                    data[j] = data[j-1]
                    j -= 1
                data [j] = tmp

def shell_sort(data):
    gap = len(data) // 2
    while gap > 0:
        for i in range(gap, len(data)):
            tmp = data[i]
            j = i - gap
            while j >= 0 and tmp < data[j]:
                data[j+gap] = data[j]


def marge_sort(data):
    mid = len(data)
    if mid == 1:
        #要素数が１以下ならそのまま返す
        return data

    #リストを分割して再帰ソート
    #left = marge_sort(data[:(mid//2)]) #左半分
    #right = marge_sort(data[(mid//2):]) #右半分

    #リストを分割
    left = data[:(mid//2)] #左半分
    right = data[(mid//2):] #右半分 
    left = marge_sort(left)
    right = marge_sort(right)
        
    #分割したリストをマージする
    array = []
    while len(left) != 0 and len(right) != 0:
        if left[0] < right[0]:
            array.append(left.pop(0))
        else:
            array.append(right.pop(0))

    if len(left) != 0:
        #左側にデータが残っていたら末尾にマージ
        array.extend(left)
    elif len(right) != 0:
        #右側にデータが残っていたら末尾にマージ
        array.extend(right)

    return array

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
    if len(data) < 64:
        return insertion_sort(data)
    #print(len(data))
    pivot = data[0]
    #配列の２つを比べて小さい方を基準にする
    if len(data) > 2:
        pivot = data[1] if data[1] < data[0]  else data[0]
    #CENTER = data[(len(data) // 2):(len(data) // 2+1)]
    #point = data[CENTER]
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
    

if __name__ == '__main__':
    import time
    import sys
     
    '''
    start = time.time()
    for _ in range(LOOP_COUNT):
        data = data_generate()
        selection_sort(data)
        print(',', end='' )
        sys.stdout.flush()

    end = time.time()
    print()
    print('経過時間、', (end-start))
    print('平均時間、', ((end-start) / LOOP_COUNT))
    # data = data_generate()
    # selection_sort(data)
    # print(data)
    '''
    '''
    start = time.time()
    for _ in range(LOOP_COUNT):
        data = data_generate()
        bubble_sort(data)
        [print(',', end='' ) if _ % 100 != 99 else print(int(_ / 100 + 1))]
        sys.stdout.flush()
    end = time.time()
    print()
    print('経過時間、', (end-start))
    print('平均時間、', ((end-start) / LOOP_COUNT))

    #data = data_generate()
    #bubble_sort(data)
    #print(data)
    '''

    #data = data_generate()
    #insertion_sort(data)
    #print(data)
    ''' 
    start = time.time()
    for _ in range(LOOP_COUNT):
        data = data_generate()
        insertion_sort(data)
        [print(',', end='' ) if _ % 100 != 99 else print(int(_ / 100 + 1))]
        sys.stdout.flush()
    end = time.time()
    print()
    print('経過時間、', (end-start))
    print('平均時間、', ((end-start) / LOOP_COUNT))

    #data = data_generate()
    #a =  marge_sort(data)
    #print(a)

    start = time.time()
    for _ in range(LOOP_COUNT):
        data = data_generate()
        marge_sort(data)
        [print(',', end='' ) if _ % 100 != 99 else print(int(_ / 100 + 1))]
        sys.stdout.flush()
    end = time.time()
    print()
    print('経過時間、', (end-start))
    print('平均時間、', ((end-start) / LOOP_COUNT))
    

    #data = data_generate()
    #a = quick_sort(data)
    #print(a)
    

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
    ''' 
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
