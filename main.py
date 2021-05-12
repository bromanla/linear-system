import sys
import argparse
import generate
import solve

parser = argparse.ArgumentParser()

parser.add_argument(
    '-g', '--generate',
    help = 'Generate koef.txt file',
    action = 'store_true'
)

parser.add_argument(
    '-c', '--count',
    help = 'Set the dimension of the matrix',
    type = int,
    default = 2
)

parser.add_argument(
    '-f', '--file',
    help = 'Specify file path',
    default = 'koef.txt'
)

configuration = parser.parse_args(sys.argv[1:])

print('--- configuration ---')
print('generate = {}'.format(configuration.generate))
print('count = {}'.format(configuration.count))
print('file = {}'.format(configuration.file))

# --- Generate koef.txt  --- #
if (configuration.generate == True):
    generate.start(configuration)

# --- Main program --- #
if (configuration.generate == False):
    solve.start(configuration)
