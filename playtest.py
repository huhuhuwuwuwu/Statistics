#!/usr/bin/env python
# coding: utf-8
# uid,
# 动画 anime
# 音乐 music
# 游戏 game
# 娱乐 enc
# 电视剧 teleplay
# 番剧 bangumi
# 电影 movie
# 科技 tech
# 鬼畜 kich
# 舞蹈 dance


def run(playfile):
    playfile = file(playfile, 'r')
    lines = playfile.readlines()
    usercount = 0
    playArray = []
    for line in lines:
        playdict = line.split(',')
        usercount += 1
        playsumdict = sum(int(n) for n in playdict[1:11])
        playdict.append(playsumdict)
        if playsumdict == 0:
            continue
        playArray.append(playdict)
        # print '%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%d' %(playdict[0],\
        #  playdict[1], playdict[2], playdict[3], playdict[4],\
        #  playdict[5], playdict[6], playdict[7], playdict[8],\
        #  playdict[9], playdict[10][0:-1], playdict[11])
    print usercount
    return playArray


def playsort(workArray):
    # workArray.sort(cmp = lambda x,y:cmp(x[11],y[11]))
    playcount_0to50 = 0 # 0 - 50
    playcount_50to100 = 0 # 50 - 100
    playcount_100to200 = 0 # 100 - 200
    playuid_100to200_2013 = 0 # 0 - 887000
    playuid_100to200_2013_sum = 0
    playuid_100to200_2014 = 0 # 887000 -
    playuid_100to200_2014_sum = 0
    playcount_200to = 0 # 200 - 
    for item in workArray:
        # print '%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%d' %(item[0],\
        #  item[1], item[2], item[3], item[4],\
        #  item[5], item[6], item[7], item[8],\
        #  item[9], item[10][0:-1], int(item[11]))  
        # if int(item[11]) <= 50:
        # # 50 100 200 
        #      playcount_0to50 += 1
        # if 100 < int(item[11]) <= 200:
        #     playcount_100to200 += 1
        if int(item[0]) <= 887000:
            playuid_100to200_2013 += 1
            playuid_100to200_2013_sum = playuid_100to200_2013_sum + int(item[11])
        if 887000 < int(item[0]):
            playuid_100to200_2014 += 1
            playuid_100to200_2014_sum = playuid_100to200_2014_sum + int(item[11])
        #     print '%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%d' %(item[0],\
        #          item[1], item[2], item[3], item[4],\
        #          item[5], item[6], item[7], item[8],\
        #          item[9], item[10][0:-1], int(item[11]))
    # print 'playcount100 - 200:', playcount_100to200
    print 'uid and sum:',playuid_100to200_2013, playuid_100to200_2014, playuid_100to200_2013_sum, playuid_100to200_2014_sum
    print 'avg:', playuid_100to200_2013_sum / playuid_100to200_2013, playuid_100to200_2014_sum / playuid_100to200_2014


if __name__ == '__main__':
    playArray = run('./mmview.csv')
    playsort(playArray)
