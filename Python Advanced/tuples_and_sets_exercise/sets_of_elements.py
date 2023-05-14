nums = [int(num) for num in input().split()]
n = nums[0]
m = nums[1]

n_set = set()
m_set = set()

for _ in range(n):
    number = int(input())
    n_set.add(number)

for _ in range(m):
    number = int(input())
    m_set.add(number)

intersection = n_set.intersection(m_set)

print(*intersection, sep="\n")