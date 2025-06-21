import sys


def main():
    input = sys.stdin.readline
    N, Q = map(int, input().split())
    data = [(-1, "")]    
    server_ptr = 0
    pc_ptr = [0] * N
    for _ in range(Q):
        query = input().split()
        q_type = int(query[0])
        if q_type == 1:
            p = int(query[1]) - 1
            pc_ptr[p] = server_ptr
        elif q_type == 2:
            p = int(query[1]) - 1
            s = query[2]
            base_ptr = pc_ptr[p]
            new_ptr = len(data)
            data.append((base_ptr, s))
            pc_ptr[p] = new_ptr
        elif q_type == 3:
            p = int(query[1]) - 1
            server_ptr = pc_ptr[p]

    result_parts = []
    ptr = server_ptr
    while ptr != -1:
        base_ptr, s = data[ptr]
        result_parts.append(s)
        ptr = base_ptr
    
    final_string = "".join(reversed(result_parts))
    print(final_string)

if __name__ == "__main__":
    main()
