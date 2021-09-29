def solution(sizes):
    w = []
    h = []
    for i in range(len(sizes)):
        w.append(max(sizes[i]))
        h.append(min(sizes[i]))
    return max(w)*max(h)
