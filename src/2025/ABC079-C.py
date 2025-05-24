abcd = list(map(int, list(input().strip())))
op=['+', '-']

for op1 in op:
    for op2 in op:
        for op3 in op:
            a=abcd[0]
            b=abcd[1]
            c=abcd[2]
            d=abcd[3]
            if eval(f'{a}{op1}{b}{op2}{c}{op3}{d}')==7:
                print(f'{a}{op1}{b}{op2}{c}{op3}{d}=7')
                exit()
