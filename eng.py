import random


class Reg:    
    def __init__(self, n, m):
        self.val = []
        self.max = m
        for i in range(n):
            self.val.append(random.randint(0, m - 1))
        self.count = n

    def write(self):
        names = "abcdefghijklmnopqrstuvwxyz"
        for i in range(self.count):
            print names[i], '\t',
#        print '\tx\ty'
        print
        for i in range(self.count):
            print self.val[i], '\t',
#        print '\t', self.tmp[0], '\t', self.tmp[1]
        print
        print

    def myInit(self, v, m):
        self.val = v
        self.max = m
        self.count = len(self.val)


class Program:
    def new(self, c, n):
        self.val = []
        self.count = c
        for i in range(c):
            tmp = []
            op = random.randint(0, 4)
            if op == 0:
                tmp.append("add")
            elif op == 1:
                tmp.append("mul")
            elif op == 2:
                tmp.append("inc")
            elif op == 3:
                tmp.append("mov")
            elif op == 4:
                tmp.append("xchg")

            if op == 2:
                tmp.append(random.randint(0, n - 1))
            else:
                tmp.append(random.randint(0, n - 1))
                tmp.append(random.randint(0, n - 1))
            
            self.val.append(tmp)

    def write(self):
        names = "abcdefghijklmnopqrstuvwxyz"
        
        for i in range(self.count):
            if self.val[i][0] != "inc":
                print self.val[i][0], "%s, %s" % (names[self.val[i][1]], names[self.val[i][2]])
            else:
                print self.val[i][0], names[self.val[i][1]]

    def make(self, reg):
        for i in range(self.count):
            cmd = self.val[i]
            op = cmd[0]
            if op == "add":
                add = reg.val[cmd[1]] + reg.val[cmd[2]]
                a = cmd[1]
                p = reg.val[cmd[1]] // reg.max
                reg.val[cmd[1]] = add % reg.max
                while a != 0 and p != 0:
                    a += 1
                    reg.val[a] += p
                    p = reg.val[a] // reg.max
                    reg.val[a] = add % reg.max
            elif op == "mul":
                mul = reg.val[cmd[1]] * reg.val[cmd[2]]
                reg.val[cmd[1]] = mul // reg.max
                reg.val[cmd[2]] = mul % reg.max
            elif op == "inc":
                reg.val[cmd[1]] += 1
                a = cmd[1]
                p = reg.val[a] // reg.max
                while a != 0 and p != 0:
                    a += 1
                    reg.val[a] += p
                    p = reg.val[a] // reg.max
                    reg.val[a] = add % reg.max
            elif op == "mov":
                reg.val[cmd[1]] = reg.val[cmd[2]]
            elif op == "xchg":
                reg.val[cmd[1]], reg.val[cmd[2]] = reg.val[cmd[2]], reg.val[cmd[1]]















