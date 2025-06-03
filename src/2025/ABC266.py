x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
x4, y4 = map(int, input().split())

def is_convex_quadrilateral(points):
    """四角形が凸であるか判定する"""
    def cross_product(v1, v2):
        return v1[0] * v2[1] - v1[1] * v2[0]

    for i in range(4):
        p_prev = points[i - 1]
        p_curr = points[i]
        p_next = points[(i + 1) % 4]
        v1 = (p_next[0] - p_curr[0], p_next[1] - p_curr[1])
        v2 = (p_prev[0] - p_curr[0], p_prev[1] - p_curr[1])
        if cross_product(v1, v2) <= 0:
            return False
    return True

square = [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]
if is_convex_quadrilateral(square):
    print("Yes")
else:
    print("No")
