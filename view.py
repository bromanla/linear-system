import sys

def matrix (message, matrix):
    print ('\n--- {} ---'.format(message))

    for equation in matrix:
        print (equation)

def result (matrix):
    view = '\n--- result ---\n'

    for i, value in enumerate(matrix):
        view += 'x{0} = {1}\n'.format(i, value)

    print (view)

def error (message):
    print('---! {} !---'.format(message))
    sys.exit()
