def vector_size_check(*vector_variables):
    return len(set([len(vector_variable) for vector_variable in vector_variables])) == 1


def vector_addition(*vector_variables):
    if not vector_size_check(*vector_variables):
        raise ArithmeticError
    return [sum(vector_variable) for vector_variable in zip(*vector_variables)]


def vector_subtraction(*vector_variables):
    if not vector_size_check(*vector_variables):
        raise ArithmeticError
    sub = [-1*sum(vector_variable) for vector_variable in zip(*vector_variables)]
    sumz = [sum(x) for x in zip(vector_variables[0], sub)]
    result = [sum(x) for x in zip(vector_variables[0], sumz)]
    return result

def scalar_vector_product(alpha, vector_variable):
    return [alpha*x for x in vector_variable]


def matrix_size_check(*matrix_variables):
    return len(set([len(marix) for marix in matrix_variables])) == 1 and len(set([len(marix[0]) for marix in matrix_variables])) == 1


def is_matrix_equal(*matrix_variables):
    return matrix_size_check(*matrix_variables)


def matrix_addition(*matrix_variables):
    if not matrix_size_check(*matrix_variables):
        raise ArithmeticError
    return [[sum(row) for row in zip(*x)] for x in zip(*matrix_variables)]


def matrix_subtraction(*matrix_variables):
    if not matrix_size_check(*matrix_variables):
        raise ArithmeticError
    sub = [[-1*sum(row) for row in zip(*x)] for x in zip(*matrix_variables)]
    sumz = matrix_addition(matrix_variables[0], sub)
    result = matrix_addition(matrix_variables[0], sumz)
    return result


def matrix_transpose(matrix_variable):
    return [[element for element in x] for x in zip(*matrix_variable)]


def scalar_matrix_product(alpha, matrix_variable):
    return [[alpha*x for x in vector] for vector in (matrix_variable)]


def is_product_availability_matrix(matrix_a, matrix_b):
    return len(matrix_a) == len(matrix_b[0])


def matrix_product(matrix_a, matrix_b):
    if not is_product_availability_matrix(matrix_a, matrix_b):
        raise ArithmeticError
    return [[sum(a*b for a, b in zip(vector_b_colum, vector_a)) for vector_b_colum in zip(*matrix_b)] for vector_a in (matrix_a)]
