#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
用栈模拟汉诺塔问题

src: A, des: B, buf: C
mov(n-1, A->C, B)
mov(1, A->B)
mov(n-1, C->B, A)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/3/20
"""


class Tower(object):
    # create three towers (i from 0 to 2)
    def __init__(self, i):
        self.disks = []

    # Add a disk into this tower
    def add(self, d):
        if len(self.disks) > 0 and self.disks[-1] <= d:
            print("Error placing disk %s" % d)
        else:
            self.disks.append(d)

    # @param {Tower} t a tower
    # Move the top disk of this tower to the top of t.
    def move_top_to(self, t):
        # Write your code here
        t.add(self.disks.pop())

    # @param {int} n an integer
    # @param {Tower} destination a tower
    # @param {Tower} buffer a tower
    # Move n Disks from this tower to destination by buffer tower
    def move_disks(self, n, destination, buffer):
        # Write your code here
        if n > 0:
            self.move_disks(n-1, buffer, destination)
            self.move_top_to(destination)
            buffer.move_disks(n-1, destination, self)

    def get_disks(self):
        return self.disks


if __name__ == "__main__":
    # Your Tower object will be instantiated and called as such:
    towers = [Tower(0), Tower(1), Tower(2)]
    n = 3
    for i in range(n - 1, -1, -1):
        towers[0].add(i)
    towers[0].move_disks(n, towers[2], towers[1])
    print(towers[0].get_disks(), towers[1].get_disks(), towers[2].get_disks())
