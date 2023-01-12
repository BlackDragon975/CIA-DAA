import random

random.seed(69)
match = 5
mismatch = -4

def generate_string(length, count):
    if length == 0:
        return ""
    else:
        letters = ['A'] * count['A'] + ['C'] * count['C'] + ['G'] * count['G'] + ['T'] * count['T']
        return random.choice(letters) + generate_string(length - 1, count)

count = {'A' : 4, 'C' : 4, 'G' : 4, 'T' : 4}

genome_1 = generate_string(16, count)
genome_2 = generate_string(16, count)

alignment_matrix = [[0 for x in range(17)] for y in range(17)]


def print_matrix(matrix, i, j, c, flag=0):
    if flag == 0:
        print('    ', end = '')
        for x in genome_1:
            print(x, end = ' ')
        print()
        print('  ', end='')
        flag = 1
    if i == len(matrix):
        return
    if j == len(matrix[i]):
        print()
        if c != 16:
            print(genome_2[c], end = ' ')
        print_matrix(matrix, i+1, 0, c+1, 1)
    else:
        print(matrix[i][j], end = ' ')
        print_matrix(matrix, i, j+1, c, 1)
        

print(genome_1)
print(genome_2)
print()
print_matrix(alignment_matrix, 0, 0, 0)

