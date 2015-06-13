import fileinput, sys
import time


def main():
    start = time.clock()

    with open('.input', 'r') as input:
        T = int(input.readline())


        with open('.output', 'w') as output:
            for case in range(1,T+1):
                K, N = [int(x) for x in input.readline().split()]

                output.write("Case #%d: %s" % (case, answer))

            output.write(str(time.clock() - start))

            

