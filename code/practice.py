# File for questions and answers

# Print each item in a list
A = [1,2,3,4,5]
for a in A:
    print(a)

print('',end='\n')
i = 0
while i < len(A):
    print(A[i])
    i += 1

# For each item in the list, print its neighbor
# there is only 1 neighbor on the ends
A = [1,2,3,4,5]
i = 0
while i < len(A):
    if i == 0:
        print('Neighbor of %s is: %s' % (A[i], A[i+1]))
    elif i == len(A) - 1:
        print('Neighbor of %s is: %s' % (A[i], A[i-1]))
    else:
        print('Neighbors of %s are %s and %s' % (A[i], A[i-1], A[i+1]))
    i += 1