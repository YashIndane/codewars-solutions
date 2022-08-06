def is_triangle(a, b, c):
    return all([a + b > c , a+ c > b , c + b>a])
