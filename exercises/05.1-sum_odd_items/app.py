my_list = [4,5,734,43,45,100,4,56,23,67,23,58,45]

# Your code here
def sum_odds(list):
    sum=0
    for i in list:
        if i%2!=0:
            sum+=i
    return sum

print(sum_odds(my_list))
