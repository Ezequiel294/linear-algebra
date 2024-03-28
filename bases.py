import numpy as np


def gram_schmidt(vectors):
    basis = []
    for v in vectors:
        w = v - np.sum(np.dot(v, b) / np.dot(b, b) * b for b in basis)
        if not np.allclose(w, 0):
            basis.append(w)
    return basis


amountOfVectors = int(input("Enter the amount of vectors: "))
dimensionsOfVectors = int(input("Enter the dimensions of your vectors: "))

vectors = []

for i in range(amountOfVectors):
    vector = []
    for j in range(dimensionsOfVectors):
        vector.append(float(input(f"Enter element v_{i+1}[{j+1}]: ")))
    vectors.append(vector)
    print("\n")

npVectors = np.array(vectors)
basis = gram_schmidt(npVectors)

for i, vector in enumerate(basis):
    print(f"Vector {i+1}: {vector}")
