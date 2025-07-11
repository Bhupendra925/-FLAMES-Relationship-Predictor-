name1 = list(input("Enter your name : ").lower())
name2 = list(input("Enter your  partner\s name: ").lower())

for latter in name1[:]: #[] ye slice karega remove karne ke bad suru se count / read karega word ko
    if latter in name2:
        name1.remove(latter)
        name2.remove(latter)
    
count = len(name1)+ len(name2)

flames = ["Friends" , " Love" , "Affection" , " Marrige" , "Enemy" ,"Sibling"]

i =0
current_count =0

while len(flames)> 1:
    if current_count == count - 1:
        flames.pop(i)
        current_count =0
    i = (i+1)% len(flames)
    current_count += 1

print( "Your Reletionshipis :- ", flames[0])
