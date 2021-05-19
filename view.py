import sys

def matrix (message, matrix):
    print ('\n--- {} ---'.format(message))

    for equation in matrix:
        print (equation)

def result (matrix, message = 'result'):
    view = '\n--- {0} ---\n'.format(message)

    for i, value in enumerate(matrix):
        view += 'x{0} = {1}\n'.format(i, value)

    print (view)

def error (message):
    print('---! {} !---'.format(message))
    sys.exit()

def comparison (native, numpy):
    print('--- comparison (round 2) ---')

    for i in range(len(native)):
        if round(native[i], 2) == round(numpy[i], 2):
            print('x{0} OK'.format(i))
        else:
            print('x{0} Err'.format(i))
