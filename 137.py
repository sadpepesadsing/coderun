import sys


def main():
    k = int(input())
    coords = [list(map(int, input().split())) for _ in range(k)]
    x_minimum, y_minimum = 10**9+1, 10**9+1
    x_maximum, y_maximum = 0, 0
    for point in coords:
        x_maximum = max(x_maximum, point[0])
        x_minimum = min(x_minimum, point[0])
        y_maximum = max(y_maximum, point[1])
        y_minimum = min(y_minimum, point[1])
    print(x_minimum, y_minimum, x_maximum, y_maximum)

if __name__ == '__main__':
    main()
