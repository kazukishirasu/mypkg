#!/usr/bin/env python3
import rospy
import math
import random
from std_msgs.msg import Int32

n = 0
r = 0
def cb(message):
    global n
    n = message.data

rospy.init_node('twice')
sub = rospy.Subscriber('count_up', Int32, cb)
pub = rospy.Publisher('twice', Int32, queue_size=1)
rate = rospy.Rate(10)

a = random.randint(31,3100)
ans = (n + a) % 31
print(ans)
while 1:
    while 1:
        x = int(input("0～30までの数字を入力してね:"))
        if x < 0 or x > 30:
            print("↑よく読んでね")
        else:
            break
    r += 1
    if x == ans:
        print("正解!おめでとう！")
        if r == 1:
            print("score:100")
        elif r == 2:
            print("score:90")
        elif r == 3:
            print("score:80")
        elif r == 4:
            print("score:70")
        elif r == 5:
            print("score:60")
        elif r == 6:
            print("score:50")
        elif r == 7:
            print("score:40")
        elif r == 8:
            print("score:30")
        elif r == 9:
            print("score:20")
        elif r == 10:
            print("score:10")
        else:
            print("score:0")
        break
    elif ans - x >= 10:
        print("もっと上だよ！")
    elif x - ans >= 10:
        print("もっと下だよ！")
    elif x < ans:
        print("もう少し上だよ！")
    elif x > ans:
        print("もう少し下だよ！")

while not rospy.is_shutdown():
    rospy.signal_shutdown('finish')
    rospy.spin()
