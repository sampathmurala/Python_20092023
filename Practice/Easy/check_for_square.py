# Given coordinates of four points in a plane, find if the four points form a square or not.
# a) All four sides formed by points are the same.
# b) The angle between any two sides is 90 degree.
# c) Check both the diagonals have the same distance.

def distance(point1, point2):
    return ((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2) ** 0.5


def doesFormSquare(points):
    distances = []
    # Calculate distances between all pairs of points
    for p in range(len(points)):
        for q in range(p + 1, len(points)):
            distances.append(distance(points[p], points[q]))

    # Identify unique distances
    distances.sort()
    unique_distances = set(distances)

    # 1. Check if there are two unique distances
    # 2. Check if the ratio of longer distance to shorter distance is sqrt(2)
    # 3. Check if the remaining two distances are equal to the shorter distance
    if len(unique_distances) == 2:
        if max(unique_distances) / min(unique_distances) == (2 ** 0.5):
            if distances.count(distances[4]) == 2 and distances.count(distances[0]) == 4:
                print("The points form a square.")
                return True

    print("The points do not form a square.")
    return False


coordinates = [(0, 0), (1, 1), (1, 0), (4, 1)]
doesFormSquare(coordinates)
