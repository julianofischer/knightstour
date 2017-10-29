import numpy as np

# GENERAL TO DO: refactoring
def valid_position(x, y, n):
    return x >= 0 and x < n  and y >= 0 and y < n


# i: linha inicial
# j: coluna inicial
def gen_valid_moves(i, j, n):
    li = list()
    possible_i = [-2, +2, -1, +1]
    possible_j = [-2, +2, -1, +1]

    for x in possible_i:
        for y in possible_j:
            if abs(x) != abs(y):
                t = (i+x, j+y)
                if valid_position(t[0], t[1], n):
                    li.append(t)

    return li


def gen_initial_moves(n):
    i = range(n)
    j = range(n)
    return [(x, y) for x in i for y in j]


def gen_zeroes_matrix(n):
    m = []
    for i in range(n):
        line = [0] * n
        m.append(line)

    return m


def trysolution(i, j, m, n, depth):
    # print("i:%d, j:%d, depth:%d" % (i, j, depth))

    if m[i][j] == 0:
        m[i][j] = depth

        if depth == n**2:
            return True

        valid_moves = gen_valid_moves(i, j, n)

        while len(valid_moves) > 0:
            move = valid_moves.pop(0)
            r = trysolution(move[0], move[1], m, n, depth + 1)
            if r:
                return True

        # cancel record
        m[i][j] = 0
        return False
    else:
        return False

nrof_solutions = 0


def tryallsolutions(i, j, m, n, depth):
    # print("i:%d, j:%d, depth:%d" % (i, j, depth))
    global nrof_solutions

    if m[i][j] == 0:
        m[i][j] = depth

        if depth == n ** 2:
            nrof_solutions = nrof_solutions + 1
            #print(np.matrix(m))
            m[i][j] = 0
            return True

        valid_moves = gen_valid_moves(i, j, n)

        while len(valid_moves) > 0:
            move = valid_moves.pop(0)
            tryallsolutions(move[0], move[1], m, n, depth + 1)

        # cancel record
        m[i][j] = 0
        return False
    else:
        return False


# i,j: initial position
def run(i, j, n):
    m = gen_zeroes_matrix(n)
    trysolution(i, j, m, n, 1)
    print(np.matrix(m))


# equivalent above
def run_first_position(i, j, n):
    m = gen_zeroes_matrix(n)
    m[i][j] = 1
    depth = 1
    valid_moves = gen_valid_moves(i, j, n)

    move = valid_moves.pop(0)
    while not trysolution(move[0], move[1], m, n, depth + 1) and len(valid_moves) > 0:
        move = valid_moves.pop(0)
    print(np.matrix(m))


def run_all_solutions_from_initial_position(i, j, n):
    m = gen_zeroes_matrix(n)
    m[i][j] = 1
    depth = 1
    valid_moves = gen_valid_moves(i, j, n)

    while len(valid_moves) > 0:
        move = valid_moves.pop(0)
        tryallsolutions(move[0], move[1], m, n, depth + 1)

    print("Number of solutions %d" % nrof_solutions)


def run_all_solutions(n):
    all_positions = [(x, y) for x in range(n) for y in range(n)]

    for position in all_positions:
        m = gen_zeroes_matrix(n)
        tryallsolutions(position[0], position[1], m, n, 1)

# run(2, 2, 5)
# run_first_position(2, 2, 5)
# run_all_solutions_from_initial_position(2, 2, 5)
run_all_solutions(5)
print("Nrof solutions %d" % nrof_solutions)
