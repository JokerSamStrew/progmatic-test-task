import re


def possible_insertion_index(expr):
    for i in range(4,9):
        index = expr.rfind(str(i))
        if index != -1:
            return index
    return -1

def split_expression(index, expr):
    head, tail = expr[:index], expr[index:]

    return head, tail

def calculate_expression(ariphmetic_expr):
    if eval(ariphmetic_expr) == 200:
        return ariphmetic_expr

    index = possible_insertion_index(ariphmetic_expr)
    if index == -1:
        raise RuntimeException('Not found possible insertion places')

    return '98 + 76 - 5 + 43 - 2 - 10' 

if __name__ == "__main__":
   print(calculate_expression(input()))
