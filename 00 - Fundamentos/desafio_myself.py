"""
T = input()

### 1
T = input()


if len(T) <= 140:
    print("TWEET")
else:
    print(str("MUTE"))
"""

"""
month = input()

months_dict = {
  "1": "January",
  "2": "February",
  "3":"March",
  "4":"April",
  "5":"May",
  "6":"June",
  "7":"July",
  "8":"August",
  "9":"September",
  "10":"October",
  "11":"November",
  "12":"December"
}

x = months_dict[f"{month}"]
print(x)
"""


N = int(input())


if N > 0:
    for _ in range(N):
        A, B = input().split()

        if A.endswith(B):
            print("encaixa")
        else:
            print("nao encaixa")



""" # submetido

N = int(input())

for _ in range(N):
    A, B = input().split()

    if A.endswith(B):
        print("encaixa")
    else:
        print("nao encaixa") """