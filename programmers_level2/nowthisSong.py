# https://programmers.co.kr/learn/courses/30/lessons/17683
import math


def solution(m, musicinfos):
    answer = []
    m = m.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")
    for i in musicinfos:
        start, end, title, song = i.split(",")
        start_h, start_m = start.split(":")
        end_h, end_m = end.split(":")

        start_t, end_t = int(start_h) * 60 + int(start_m), int(end_h) * 60 + int(end_m)
        clock = end_t - start_t

        song = song.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")

        song *= math.ceil(clock / len(song))  # 남은 시간만큼 문자열을 늘려줌
        song = song[:clock]
        if m not in song:
            continue
        answer.append([i, clock, title])
    answer.sort(key=lambda x: (-x[1], x[0]))  # 조건 이만족한게 여러개면 노래시간이 긴순, 먼저 입력된 순
    return answer[0][2] if answer else "(None)"


print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
