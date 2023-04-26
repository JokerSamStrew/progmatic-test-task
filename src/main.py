def tokens_sum(tokens):
    return sum([int(op + value) for op, value in tokens])

def tokens_to_str(tokens):
    return ' '.join([op + ' ' + value for op, value in tokens]).strip()

def tokens_variety(tokens, number, result):
    if number == -1:
        if tokens_sum(tokens) == 200:
            result.append(tokens)
        return

    tokens_variety(tokens + [('+', str(number))], number - 1, result)
    tokens_variety(tokens + [('-', str(number))], number - 1, result)
    op, value = tokens[-1]
    tokens_variety(tokens[:-1] + [(op, value + str(number))], number - 1, result)



def calculate_expressions():
    results = []
    tokens_variety([('', '9')], 8, results) 
    for result in results:
        str_result = tokens_to_str(result)
        print(str_result, ' = ', eval(str_result))

if __name__ == "__main__":
    calculate_expressions()
