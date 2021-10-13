import numpy as np

m_a = np.matrix((
    (1, 1, 2),
    (-3, 2, -1),
    (-1, 4, 5)
    ))

v_a = np.matrix((
    [4], 
    [2], 
    [-3]
))

def dot(a, b):
    return sum(i * j for i, j in zip(a, b))

print("1.", 2 * m_a)
print("2.", m_a * v_a)
print("3.", dot(-2 * m_a * v_a, v_a))
print("=" * 20)

print(np.linalg.solve(
    np.matrix((
        (2, 3, 1, 1),
        (0, -2, 6, 18),
        (0, 0, -16, -20),
        (0, 0, 8, 36)
        )), np.matrix((
        [4], 
        [-40], 
        [40],
        [88]
        ))
    )
)

m_b = np.matrix((
    (-150, -423, 33, 99),
    (86, 820, 62, -924),
    (-193, 295, -13, -742),
    (-112, 152, -123, 147),
    (-135, -160, -13, -76)
))

print(np.linalg.matrix_rank(m_b))