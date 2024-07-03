list_of_numbers = [4, 80, 85, 59, 37, 25, 5, 64, 66, 81, 20, 64, 41, 22, 76, 76, 55, 96, 2, 68]

# Your code here
def sort_odd_even(list):
    sorted_list=[]
    for j in list:
        if j%2==0:
            sorted_list.append(j)
    for i in list:
        if i%2!=0:
            sorted_list.append(i)
    print(len(sorted_list))
    return sorted_list




print(sort_odd_even(list_of_numbers))
print(len(list_of_numbers))

