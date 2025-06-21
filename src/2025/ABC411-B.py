

def main():
  N = int(input())
  if N == 1:
      return
  D = list(map(int, input().split()))
  for i in range(N - 1):
      distances_for_row = []
      current_sum = 0
      for j in range(i, N - 1):
          current_sum += D[j]
          distances_for_row.append(current_sum)
      print(*distances_for_row)


if __name__ == "__main__":
    main()
