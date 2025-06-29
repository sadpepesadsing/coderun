import sys

def make_sum_map(n, m, origin_map):
    summs_map = [[0 for i in range(m)] for g in range(n)]
    summs_map[0][0] = origin_map[0][0]

    for i in range(1, m):
        summs_map[0][i] = summs_map[0][i-1] + origin_map[0][i]
    
    for i in range(1, n):
        summs_map[i][0] = summs_map[i-1][0] + origin_map[i][0]

    for i in range(1, m):
        for g in range(1, n):
            summs_map[g][i] = max(summs_map[g-1][i], summs_map[g][i-1]) + origin_map[g][i]
    
    return summs_map

def make_road(n, m, summs_map):
    road = []
    i, g = n-1, m-1

    while i + g != 0:
        if i > 0 and g > 0:
            if summs_map[i-1][g] > summs_map[i][g-1]:
                road.append('D')
                i -= 1
            else:
                road.append('R')
                g -= 1
        elif i > 0:
            road.append('D')
            i -= 1
        else:
            road.append('R')
            g -= 1
    return ' '.join(road[::-1])

def main():
    n, m = tuple(list(map(int, input().split())))
    origin_map = []

    for _ in range(n):
        origin_map.append(list(map(int, input().split())))

    summs_map = make_sum_map(n, m, origin_map)
    print(summs_map[n-1][m-1])
    print(make_road(n, m, summs_map))

if __name__ == '__main__':
    main()
