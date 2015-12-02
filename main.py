import eng


COUNT = 4
MAX = 100
a = ' '

while a != 'q':
    reg = eng.Reg(COUNT, MAX)
    reg.myInit([99, 99, 99, 99], 100)
    prog = eng.Program()

    reg.write()

    prog.new(5, 4)
    prog.write()

    a = raw_input()

    prog.make(reg)
    reg.write()
