#!/usr/bin/python3
""" creating the matrix multiplication"""

def matrix_mul(m_a, m_b):
    """creation of the function to multiply matrices
    Args:
        m_a: first matrix
        m_b: second matrix

    Raises:
        TypeError: an error that occurs if variable is not of a
        specific datatype
        ValueError: an error generated by an empty list
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    for list1 in m_a:
        if not isinstance(list1, list):
            raise TypeError("m_a must be a list of lists")
    if all(not isinstance(list2, list) for list2 in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_a == [] and m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] and m_b == [[]]:
        raise ValueError("m_b can't be empty")
    if all(not isinstance(nums, (int, float)) for row in m_a for nums in row):
        raise TypeError("m_a should contain only integers or floats")
    if all(not isinstance(nums1, (int, float)) for row in
            m_b for nums1 in row):
        raise TypeError("m_b should contain only integers or floats")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]
    return (result)

if __name__ = "__main__":
    unittest.main()
