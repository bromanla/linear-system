import sys
import random

def start (configuration):
    file_text = ''

    for height in range(0, configuration.count):
        for width in range(0, configuration.count + 1):
            file_text += str(
                round(
                    random.uniform(-10, 10),
                    2
                )
            )

            if (width != configuration.count):
                file_text += '\t'

        if (height != configuration.count - 1):
            file_text += '\n'

    file = open('koef.txt', 'w')
    file.write(file_text)
    file.close()

    print('--- success ---')
    sys.exit()
