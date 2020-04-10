import random
c_num = random.randint(1, 100)
while True:
    g_num = input('請輸入猜測數字（範圍1~100）： ')
    g_num = int(g_num)
    if g_num == c_num:
        print('恭喜你～ 猜對了！')
        break
    elif g_num < c_num:
        print('好可惜～ 猜錯了！數字要再大一點唷！')
    elif g_num > c_num:
        print('好可惜～ 猜錯了！數字要再小一點唷！')
    else:
        print('請輸入數字範圍1~100之間, 謝謝你！')

