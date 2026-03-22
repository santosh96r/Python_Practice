# a = lambda x : "even" if x %2 == 0 else "odd"
#
# l1 = [12,22,65,85,36,44,11,49,25]
#
# # l2 = list(map(a, l1))
# # print(l2)
# d = {}
# for i in l1 :
#     d[i] = a(i)
#
# print(d)

# lambda arguments : expression

# add10 = lambda x : x + 10
# print(add10(52))


# points_2D = [(1,2), (15,1), (5, -1), (10,4)]
#
# # points_2D_sorted = sorted(points_2D, key = lambda x : x[1])
# #
# # print(points_2D_sorted)
#
# print(list(map(lambda x : x[1] * 2 , points_2D)))
# print(list(filter(lambda x : x[1] > 1 , points_2D)))