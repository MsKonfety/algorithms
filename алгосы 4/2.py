def bubble_sort(n, points):
    for i in range(n):
        for j in range(0, n-i-1):
            if (points[j][0] > points[j+1][0]) or (points[j][0] == points[j+1][0] and points[j][1] > points[j+1][1]):
                points[j], points[j+1] = points[j+1], points[j]

def build_polyline(n, points):
    bubble_sort(n, points)

    for x, y in points:
        print(x, y)

build_polyline(4, [(0, 0), (0, 1), (1, 0), (1, 1)])