#!/usr/bin/python3
def magic_calculation(a, b):
    answer = 0

    for integer in range(1, 3):
        try:
            if integer > a:
                raise Exception('Too far')
            answer += (a ** b) / integer
        except Exception:
            answer = b + a
            break

    return answer
