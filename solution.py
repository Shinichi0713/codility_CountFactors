def solution(N):
    # Implement your solution here
    count_split = 0
    for num in range(1, N + 1):
        if N % num == 0:
            count_split += 1
    return count_split