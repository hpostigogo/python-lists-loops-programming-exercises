
def lyrics_generator(list):
    count=1
    text=''
    for i in list:
        if i == 0:
            text+='Boom'
        elif i==1 and count<3:
            text+='Drop the bass'
            count+=1
        elif i==1 and count==3:
            text+='Drop the bass !!!Break the bass!!!'
            count=1
        text+=' '
    return text


# Your code above, nothing to change after this line
print(lyrics_generator([0,0,1,1,0,0,0]))
print(lyrics_generator([0,0,1,1,1,0,0,0]))
print(lyrics_generator([0,0,0]))
print(lyrics_generator([1,0,1]))
print(lyrics_generator([1,1,1]))
