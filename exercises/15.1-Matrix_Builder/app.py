# Your code here
def matrix_builder(number):
    list=[]
    for i in range(number):
        row=[]
        for j in range(number):
            row.append(1)
        list.append(row)

    return list

print(matrix_builder(5))