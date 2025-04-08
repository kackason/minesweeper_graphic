import numpy as np
import random
import time

M = 10
N = 8

#爆弾の個数を計算
def calcfilter(array, i, j):
    if array[i,j] != -1:
        cnt = 0
        for k in range(max(0,i-1),min(M,i+2)):
            for l in range(max(0,j-1),min(N,j+2)):
                if array[k,l] == -1:
                    cnt += 1
        array[i,j] = cnt

#ゼロのとき隣接するゼロもあける
def searchzero(array, mask, i, j):
    if array[i,j] == 0:
        for k in range(max(0,i-1),min(M,i+2)):
            for l in range(max(0,j-1),min(N,j+2)):
                if mask[k,l]=="▢":
                    mask[k,l] = array[k,l]
                    searchzero(array, mask, k, l)
    return

#nxm配列をつくる
array = np.zeros((M,N),dtype=int)

#爆弾設置(-1)
nbom = 12
lbom = []
random.seed(time.time())
while (len(lbom)<nbom):
    p = random.randrange(M)
    q = random.randrange(N)
    if not p*M+q in lbom:
        lbom.append(p*M+q)
        array[p,q] = -1

#周りの爆弾個数を計算
for i in range(M):
    for j in range(N):
        calcfilter(array, i, j)

#マスク
mask = np.zeros((M,N),dtype=str)
for i in range(M):
    for j in range(N):
        f=0
        mask[i,j] = "▢" #マス目
expl = 0
hand = 0
print(mask)
while hand < M*N:
    hand += 1
    print("hand",hand,":")
    i,j = map(int, input().split())

    #範囲外の入力
    if not i in range(M) or not j in range(N):
        print("incorrect input\n")
        hand -= 1
        continue

    #既出
    if mask[i,j] != "▢":
        print("already opened\n")
        hand -= 1
        continue

    mask[i,j] = array[i,j]
    searchzero(array, mask, i, j)   #ゼロ拡大

    #爆破
    if array[i,j] == -1:
        mask[i,j] = "●"    #爆弾
        expl = 1
        break
    print(mask,"\n")


print(mask)
if expl == 1:
    print("###########\n Game Over \n###########\n")
else:
    print("#########\n Clear!!\n #########\n")