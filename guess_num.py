import random
i = input('請輸入想猜測範圍最小數字： ')
j = input('請輸入想猜測範圍最大數字： ')
i = int(i)
j = int(j)
c_num = random.randint(i, j)
count = 0
while True:
    count += 1
    g_num = input("請輸入猜測數字（範圍 {} ~ {}）： ".format(i, j))
    g_num = int(g_num)
    if g_num == c_num:
        print('恭喜你～ 猜對了！你總共猜了', count, '次')
        break
    elif g_num < c_num and g_num > i:
        print('好可惜～ 猜錯了！數字要再大一點唷！這是你第', count, '次猜測')
    elif g_num > c_num and g_num < j:
        print('好可惜～ 猜錯了！數字要再小一點唷！這是你第', count, '次猜測')
    else:
        print("不在數字範圍 {} ~ {} 之間, 請重新輸入，謝謝你！".format(i, j))
