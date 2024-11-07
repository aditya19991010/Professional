a = [[1,2],
     [2,3]]

b = [[3,4],
     [4,2]]

c = [[0,0],
     [0,0]]

#checking error
if len(a) == len(b[0]):
    print(True)
else:
    print(False)

#Result matrix
c = [[0 for x in range(len(a))] for x in a]
print(c)

#matrix multiplication

for rows in range(len(a)):
    for columns in range(len(b[0])):
        # if rows == columns:
            for rows_b in range(len(b)):
                c[rows][columns] += a[rows][rows_b] * b[rows_b][columns]

         # else:
        #     raise ValueError
# print(c)
# for i,j in a,b:
#     for x,y in i,j:
#         for p in
#         # c = [x for x,y in i,j]
#         print(f"{x,y} and {i,j}")
#
#     print("break")


c[0][0] = a[0][0]*b[0][0] + a[0][1]*b[1][0]
c[0][1] = a[0][0]*b[0][1] + a[0][1]*b[1][1]
c[1][0] = a[1][0]*b[0][0] + a[1][1]*b[1][0]
c[1][1] = a[1][0]*b[1][0] + a[1][1]*b[1][1]



# print(c)