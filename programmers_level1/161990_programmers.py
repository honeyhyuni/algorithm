# https://school.programmers.co.kr/learn/courses/30/lessons/161990
import sys


def solution(wallpaper):
    sx, sy, ex, ey = sys.maxsize, sys.maxsize, 0, 0
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == "#":
                sx, sy = min(sx, i), min(sy, j)
                ex, ey = max(ex, i), max(ey, j)
    return [sx, sy, ex+1, ey+1]


print(solution([".#...", "..#..", "...#."]))
print(solution(["..........", ".....#....", "......##..", "...##.....", "....#....."]))
print(solution([".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."]))
print(solution(["..", "#."]))