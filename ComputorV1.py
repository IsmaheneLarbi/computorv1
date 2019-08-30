import sys

def get_degree(polynom):
    degree = int(polynom.strip().split(' ')[-1][-1])
    return degree

def get_values(polynom, degree):
    value = 0
    data = polynom.strip().split(' ')
    coeff = [0] * (degree + 1)
    for i, arg in enumerate(data):
        if (arg[0].isdigit()):
            if (i >= 1 and data[i - 1] == '-'):
                value = float(data[i]) * (-1)
            else:
                value = float(data[i])
            degree = int(data[i + 2 ][-1]) if ((i + 2) < len(data) and data[i + 2][0] == 'X') else 0
            coeff[degree] = value
    return (coeff)

def reduce(arr1, arr2):
    values = []
    for i, val in enumerate(arr1):
        if (i < len(arr1) and i < len(arr2)):
            values.append(val - arr2[i])
    return values

def is_greater_than_two(eq):
    if (len(eq) > 3):
        for value in eq[3:]:
            if value != float(0):
                return 1
    return 0

def get_discriminant(eq):
    discr = eq[1] * eq[1] - 4 * eq[0] * eq[2]
    return (discr)

# def solve(discr)
#     if (discr > 0):

def ComputorV1():
    if len(sys.argv) != 2:
        return 1
    equation = sys.argv[1]
    sides = equation.strip().split('=')
    if (get_degree(sides[0]) > get_degree(sides[1])):
        degree = get_degree(sides[0])
    else :
        degree = get_degree(sides[1])
    coeff1 = get_values(sides[0], degree)
    coeff2 = get_values(sides[1], degree)
    eq = []
    eq = reduce(coeff1, coeff2)
    if (is_greater_than_two(eq)):
        print("The polynomial degree is stricly greater than 2, I can't solve.")
        return 1
    print(get_discriminant(eq))
    # solve(get_discriminant(eq))

if (__name__ == "__main__"):
    ComputorV1()