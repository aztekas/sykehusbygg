import numpy as np
import faiss  # pip install faiss-cpu

# --- 1. Create some example vectors ---
d = 4  # dimension of vectors
nb = 5  # number of database vectors
np.random.seed(42)
vectors = np.random.random((nb, d)).astype("float32")

# --- 2. Create an index ---
index = faiss.IndexFlatL2(d)  # L2 = Euclidean distance index

# --- 3. Add vectors to the index ---
index.add(vectors)

print(f"Number of vectors in index: {index.ntotal}")

# --- 4. Create a query vector and search ---
query = np.random.random((1, d)).astype("float32")

k = 2  # number of nearest neighbors to find
distances, indices = index.search(query, k)

print("Query vector:", query)
print("Nearest neighbors' indices:", indices)
print("Distances:", distances)


# Query vector: [[0.6118529  0.13949387 0.29214466 0.36636186]]

# array([[0.37454012, 0.9507143 , 0.7319939 , 0.5986585 ],
#        [0.15601864, 0.15599452, 0.05808361, 0.8661761 ],
#        [0.601115  , 0.7080726 , 0.02058449, 0.96990985],
#        [0.83244264, 0.21233912, 0.18182497, 0.1834045 ],
#        [0.30424225, 0.52475643, 0.43194503, 0.29122913]], dtype=float32)

# Nearest neighbors' indices: [[3 4]]
# >>> print("Distances:", distances)
# Distances: [[0.0996101 0.2682406]]
