#!/usr/bin/env python
# coding: utf-8


def run(myfile):
    myfile = file(myfile, 'r')
    lines = myfile.readlines()
    count = 0
    newArray = []
    for line in lines:
        mydict = line.split(',')
        valid = True
        for value in mydict:
            if len(value) == 0:
                valid = False
                break

        if not valid:
            continue

        if mydict[1][0] == '0':
            continue

        if mydict[1][0] == '"':
            mydict[1] = mydict[1][1:-1].strip()

        newArray.append(mydict)
        count += 1
        # print "%s,%s,%s,%s,%s" %(mydict[0],mydict[1],mydict[2],mydict[3],mydict[4][0:-1])
    return newArray

    # print count


def cdncount(myArray):
    youku_count = 0
    youku_count_pass = 0
    cc_count = 0
    cc_count_pass = 0
    local_count = 0
    local_count_pass = 0
    cc_count_nopass_dx = 0
    cc_count_nopass_cu = 0
    cc_count_nopass_cmcc = 0
    cc_count_nopass_ck = 0
    cc_count_nopass_jy = 0
    local_count_nopass_dx = 0
    local_count_nopass_cu = 0
    local_count_nopass_cmcc = 0
    local_count_nopass_ck = 0
    local_count_nopass_jy = 0
    for item in myArray:
        if item[2] == 'k' and int(item[3]) > 10:
            youku_count += 1
            # print "%s,%s,%s,%s,%s" %(item[0],item[1],item[2],item[3],item[4][0:-1])
            if int(item[3]) > 200:
                youku_count_pass += 1
        if item[2] == 'cc' and int(item[3]) > 10:
            cc_count += 1
            if int(item[3]) > 200:
                cc_count_pass += 1
        if '-' in str(item[2]) and int(item[3]) > 10:
            local_count += 1
            if int(item[3]) > 200:
                local_count_pass += 1
    print 'youku = ', youku_count
    print 'youku pass = ', youku_count_pass
    print 'youku pass rate = ', int(youku_count_pass) * 100 // int(youku_count), '%'
    print 'cc = ', cc_count
    print 'cc pass = ', cc_count_pass
    print 'cc pass rate = ', int(cc_count_pass) * 100 // int(cc_count), '%'
    print 'local = ', local_count
    print 'local pass = ', local_count_pass
    print 'local pass rate = ', int(local_count_pass) * 100 // int(local_count), '%'
    for item in myArray:
        if '电信' in str(item[4]) and 10 < int(item[3]) < 200:
            if str(item[2]) == 'cc':
                cc_count_nopass_dx += 1
                # print "%s,%s,%s,%s,%s" %(item[0],item[1],item[2],item[3],item[4][0:-1])
            if '-' in str(item[2]):
                local_count_nopass_dx += 1
        if '联通' in str(item[4]) and 10 < int(item[3]) < 200:
            if str(item[2]) == 'cc':
                cc_count_nopass_cu += 1
            if '-' in str(item[2]):
                local_count_nopass_cu += 1
                # print "%s,%s,%s,%s,%s" %(item[0],item[1],item[2],item[3],item[4][0:-1])
        if ('移动' in str(item[4]) or '铁通' in str(item[4])) and 10 < int(item[3]) < 200:
            if str(item[2]) == 'cc':
                cc_count_nopass_cmcc += 1
            if '-' in str(item[2]):
                local_count_nopass_cmcc += 1
                # print "%s,%s,%s,%s,%s" %(item[0],item[1],item[2],item[3],item[4][0:-1])
        if '长' in str(item[4]) and 10 < int(item[3]) < 200:
            if str(item[2]) == 'cc':
                cc_count_nopass_ck += 1
            if '-' in str(item[2]):
                local_count_nopass_ck += 1
        if '教育网' in str(item[4]) and 10 < int(item[3]) < 200:
            if str(item[2]) == 'cc':
                cc_count_nopass_jy += 1
            if '-' in str(item[2]):
                local_count_nopass_jy += 1
        if item[2] == 'cc' and 10 < int(item[3]) < 200:
            print "%s,%s,%s,%s,%s" %(item[0],item[1],item[2],item[3],item[4][0:-1])
    print '电信nopassrate : cc = %s%%, local = %s%%' %(cc_count_nopass_dx * 100 // int(cc_count - cc_count_pass), local_count_nopass_dx * 100 // int(local_count - local_count_pass))
    print '联通nopassrate : cc = %s%%, local = %s%%' %(cc_count_nopass_cu * 100 // int(cc_count - cc_count_pass), local_count_nopass_cu * 100 // int(local_count - local_count_pass))
    print '移动nopassrate : cc = %s%%, local = %s%%' %(cc_count_nopass_cmcc * 100 // int(cc_count - cc_count_pass), local_count_nopass_cmcc * 100 // int(local_count - local_count_pass))
    print '长宽nopassrate : cc = %s%%, local = %s%%' %(cc_count_nopass_ck * 100 // int(cc_count - cc_count_pass), local_count_nopass_ck * 100 // int(local_count - local_count_pass))
    print '教育网nopassrate : cc = %s%%, local = %s%%' %(cc_count_nopass_jy * 100 // int(cc_count - cc_count_pass), local_count_nopass_jy * 100 // int(local_count - local_count_pass))
    # print '电信nopassrate : cc = %s%%' %(cc_count_nopass_dx * 100 // int(cc_count - cc_count_pass))
    # print '联通nopassrate : cc = %s%%' %(cc_count_nopass_cu * 100 // int(cc_count - cc_count_pass))
    # print '移动nopassrate : cc = %s%%' %(cc_count_nopass_cmcc * 100 // int(cc_count - cc_count_pass))
    # print '长宽nopassrate : cc = %s%%' %(cc_count_nopass_ck * 100 // int(cc_count - cc_count_pass))
    # print '教育网nopassrate : cc = %s%%' %(cc_count_nopass_jy * 100 // int(cc_count - cc_count_pass))
    # print cc_count_nopass_cu
    # print local_count_nopass_cu


if __name__ == '__main__':
    newArray = run('./cdndiagnostics1202.csv')
    cdncount(newArray)
