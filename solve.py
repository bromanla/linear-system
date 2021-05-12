import view

def start(configuration):
    try:
        # Read file
        file = open(configuration.file, 'r')
        file_text = file.read()
        file.close()

        # Split and convert to float
        values = list(
            map(
                lambda item: list(
                    map(
                        lambda el: float(el),
                        item.split('\t'))
                    ),
                file_text.split('\n')
            )
        )
    except:
        view.error('file parsing error')

    view.matrix('the given matrix', values)

    # Matrix validation
    for equation in values:
        if (len(equation) - 1 != len(values)):
            view.error('matrix set incorrectly')

    # Direct move
    try:
        for i in range(len(values) - 1):
            for j in range(i + 1, len(values)):
                factor = values[j][i] / values[i][i] * -1
                for k in range(len(values[0])):
                    values[j][k] += values[i][k] * factor

        view.matrix('upper triangular reduction', values)
    except:
        view.error('this type of matrix is not supported. look readme.md')

    # Reverse move
    try:
        result = []

        for i in range(len(values[0]) - 1):
            result.append(1.0)

        result[-1] = values[-1][-1] / values[-1][-2]

        for i in reversed(range(0, len(values) - 1)):
            cutValues = values[i][i + 1:-1]
            cutResults = result[i + 1:]
            x = values[i][i]
            y = values[i][-1]

            notX = sum(list(map(lambda x, y: x * y, cutValues, cutResults)))

            result[i] = (y - notX) / x

        view.result(result)
    except:
        view.error('no solutions')
