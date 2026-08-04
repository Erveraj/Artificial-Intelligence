# Solve: A + B = 10, A > B and both are positive integers

solutions = []

for A in range(1, 10):
    for B in range(1, 10):
        if A + B == 10 and A > B:
            solutions.append((A, B))

print("Possible solutions:")
for solution in solutions:
    print("A =", solution[0], ", B =", solution[1])