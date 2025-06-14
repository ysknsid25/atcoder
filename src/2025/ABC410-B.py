def solve():
    N, Q = map(int, input().split())
    X = list(map(int, input().split()))

    boxes = [0] * N
    results = [] 

    for x_i in X:
        if x_i >= 1:
            target_box_idx = x_i - 1
            boxes[target_box_idx] += 1
            results.append(target_box_idx + 1)
        else:
            min_balls = float('inf')
            target_box_idx = -1

            for i in range(N):
                if boxes[i] < min_balls:
                    min_balls = boxes[i]
                    target_box_idx = i
            
            boxes[target_box_idx] += 1
            results.append(target_box_idx + 1)

    print(" ".join(map(str, results)))

if __name__ == "__main__":
    solve()
