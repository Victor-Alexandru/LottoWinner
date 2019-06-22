# write_list_to_file(six_taken, "f1.txt")
# write_list_to_file(five_taken, "f2.txt")
# write_list_to_file(four_taken, "f3.txt")


# cover_list = []
# index = 1
# for six_comb in six_taken:
#     cover = 0
#     for four_comb in four_taken:
#         isCovered = True
#         for nr in four_comb:
#             if nr not in six_comb:
#                 isCovered = False
#         if isCovered:
#             cover += 1
#
#     cover_list.append(["v" + str(index), cover])
#     index += 1
#
# print(cover_list)