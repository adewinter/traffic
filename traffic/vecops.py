import numpy as np
from numpy.linalg import norm

def is_equal_opposite(vec_1, vec_2):
    """
    Tells you if two vectors are equal but opposite
    """
    m_vec_1 = norm(vec_1)
    m_vec_2 = norm(vec_2)
    is_magnitude_equal = m_vec_1 == m_vec_2
    c_zero = np.cross(vec_1, vec_2) == 0
    dot = np.dot(vec_1, vec_2)
    return is_magnitude_equal and c_zero and dot < 0

def is_opposite(vec_1, vec_2):
    c_zero = np.cross(vec_1, vec_2) == 0
    dot = np.dot(vec_1, vec_2)
    return c_zero and dot < 0

def is_same_direction(vec_1, vec_2):
    c_zero = np.cross(vec_1, vec_2) == 0
    dot = np.dot(vec_1, vec_2)
    return c_zero and dot > 0
