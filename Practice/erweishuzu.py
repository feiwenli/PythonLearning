# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here

        a = -1
        b = -1
        for x in array:
            print x
            b = b + 1
            try:
                if target < x[0]:
                    print 'break'
                    break
                elif target == x[0]:
                    return True
                if target > x[len(x)-1]:
                    a = a + 1
                elif target == x[len(x)-1]:
                    return True
            except IndexError, e:
                return False
        print 'a',a
        print 'b',b
        if b < a:
            return False
        elif b == a:
            return self.two(array[a], target)
        else:
            for m in range(a+1,b+1):
                if self.two(array[m], target):
                    return True
            return False

    def two(self, list, target):
        min = 0
        max = len(list) - 1
        while min < max:
            center = int((max+min)/2)
            if target < list[center]:
                max = center - 1
            elif target == list[center]:
                return True
            else:
                min = center + 1



s = Solution()
print s.Find(7,[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]])
print s.Find(16,[[]])