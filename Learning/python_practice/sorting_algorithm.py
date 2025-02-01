##Insertion sorting


#'''
#1. Traverse though the array
#2. target the key and compare with the next
#3. For ascending order, start from the begining
# if the next number is greater then do not swap the position,
# if the next number is less, then mark it as a key and keep on comparing
# till a number comes which is greater than the number set on the ket.'''


A = list(23,5,34,78,61)

for i in range(len(A)):
    if A[i] < A[i+1]:
        A[i+1] = A[i]
    elif A[1] < A[1+1]:
        print("sorting done")

