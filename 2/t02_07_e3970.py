n1, s1, n2, s2 = open('input.txt').readlines()
# s1, s2 = (list(map(int, s.split())) for s in (s1, s2))
s1, s2 = (s1.split(), s2.split())
# n1 = int(n1) - 1

color_count = {}
for color in s1:
    color_count[color] = color_count.get(color, 0) + 1

for i, el in enumerate(s2):
    s2[i] = str(color_count.get(el, 0))


# for i, k in enumerate(s2):
#     low = 0
#     high = n1
#     while low <= high:
#         mid = (low + high) // 2
#         guess = s1[mid]
#         if guess < k:
#             low = mid + 1
#         else:
#             high = mid - 1
#     l1 = mid + (s1[mid] < k)
#     low = l1
#     high = n1
#     while low <= high:
#         mid = (low + high) // 2
#         guess = s1[mid]
#         if guess > k:
#             high = mid - 1
#         else:
#             low = mid + 1
#     l2 = mid - (s1[mid] > k)
#     s2[i] = str(l2 - l1 + 1)

open('output.txt', 'w').write('\n'.join(s2))
