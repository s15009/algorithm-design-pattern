#!/usr/bin/python3
GU = 1
CHOKI = 2
PA = 3
DRAW = 1
WIN = 2
LOSE = 3
judge = 0
LOOPCOUNT = 2000000

def hand_generate():
    import random

    player = random.randint(1,3)
    computer = random.randint(1,3)

    return (player,computer)

def janken1(player, computer):
    if(player == GU and computer == GU):
        judge = DRAW
    elif(player == GU and computer == CHOKI):
        judge = WIN
    elif(player == GU and computer == PA):
        judge = LOSE
    elif(player == CHOKI and computer == GU):
        judge = LOSE
    elif(player == CHOKI and computer == CHOKI):
        judge = DRAW
    elif(player == CHOKI and computer == PA):
        judge = WIN
    elif (player == PA and computer == GU):
        judge = WIN
    elif(player == PA and computer == CHOKI):
        judge = LOSE
    elif(player == PA and computer == PA):
        judge = DRAW

    if(judge == DRAW):
        #print('あいこ')
        return
    elif(judge == WIN):
        #print('勝ち')
        return
    elif(judge == LOSE):
        #print('負け')
        return

def janken2 (player, computer):
    if(player == computer):
        judge = DRAW
    elif(player == GU and computer == CHOKI or
            player == CHOKI and computer == PA or
            player == PA and computer == GU):
        judge = WIN
    else:
        judge = LOSE

def janken3 (player, computer):
    DRAW2 = 0
    WIN2 = 1
    LOSE2 = 2
    judge = (player - computer + 3) % 3

    if(judge == DRAW2):
        return
    elif(judge == WIN2):
        return
    elif(judge == LOSE2):
        return

def janken4 (player, computer):
    jud = [[DRAW,WIN,LOSE],
            [LOSE,DRAW,WIN],
            [WIN,LOSE,DRAW]]

    if(jud[player - 1][computer - 1] == DRAW):
        #print('aiko')
        return
    elif(jud[player - 1][computer - 1] == WIN):
        #print('win')
        return
    elif(jud[player - 1][computer - 1] == LOSE):
        #print('lose')
        return

if __name__ == '__main__':
    import time
    import sys


    #phand, chand = hand_generate()
    #janken4(phand,chand)

    start = time.time()
    for _ in range(LOOPCOUNT):
        phand, chand = hand_generate()
        janken1(phand,chand)
        sys.stdout.flush()
    end = time.time()
    print('else if9パターン')
    print('経過時間、', (end - start))


    start = time.time()
    for _ in range(LOOPCOUNT):
        phand, chand = hand_generate()
        janken2(phand,chand)
        sys.stdout.flush()
    end = time.time()
    print('else if3パターン')
    print('経過時間、', (end - start))

    start = time.time()
    for _ in range(LOOPCOUNT):
        phand, chand = hand_generate()
        janken3(phand,chand)
        sys.stdout.flush()
    end = time.time()
    print('計算式パターン')
    print('経過時間、', (end - start))


    start = time.time()
    for _ in range(LOOPCOUNT):
        phand, chand = hand_generate()
        janken4(phand,chand)
        sys.stdout.flush()
    end = time.time()
    print('配列パターン')
    print('経過時間、', (end - start))
