#Q2. Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array

A=[5,1,6,3,4]
start=0
end=len(A)-1

while start < end:
    A[start],A[end] = A[end],A[start]
    start += 1
    end -= 1

print(A)

