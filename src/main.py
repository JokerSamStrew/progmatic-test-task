import re

def parse_expression(expr):
    return re.findall(r'([+-])?\s*(\d+)', expr)

def split_tokens(tokens):
    for i in range(4, 9):
        index = 0
        for op, value in tokens:
            if value.find(str(i)) != -1:
                return tokens[:index], tokens[index:] 
            index += 1

def tokens_sum(tokens):
    return sum([int(op + value) for op, value in tokens])

def tokens_to_str(tokens):
    return ' '.join([op + ' ' + value for op, value in tokens]).strip()

def first_modify_stratagy(tail, desired_result):
    new_tail = []
    op, value = tail[0]
    new_tail.append((op, value + '3'))
    new_tail.append(('-', '2'))
    new_tail += tail[1:]

    if tokens_sum(new_tail) == desired_result:
        return new_tail

    return []
    

def modify_tail(tail, desired_result):
    if tokens_sum(tail) == desired_result:
        return tail

    result = first_modify_stratagy(tail, desired_result)
    if len(result) > 0:
        return result


    return []


def calculate_expression(ariphmetic_expr):
    tokens = parse_expression(ariphmetic_expr)
    head, tail = split_tokens(tokens)
    head_sum = tokens_sum(head)
    modified_tail = modify_tail(tail, 200 - head_sum)

    print(head_sum, modified_tail)

    return tokens_to_str(head + modified_tail)

if __name__ == "__main__":
   print(calculate_expression(input()))
