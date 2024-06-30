
"""
#Question1
list = [2, 3, 6]
multiple=list[0]*list[1]*list[2]
print(multiple)

#Question2

ma_liste = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
for new_list in ma_liste:
    new_list = (new_list[0], new_list[1] + 1)
ma_liste.append(new_list)

sorted_liste = sorted(ma_liste, key=lambda x: x[1])
print(sorted_liste)

#question3

d1 = {'a': 100, 'b': 200, 'c':300}

d2 = {'a': 300, 'b': 200, 'd':400}

for keys in d2:
    if keys in d1:
        d1[key]+=d2[key]
    else:
        d1[key]=d2[key]

print(d1)

#Question4

n=int(input(" Veuillez entrer un nombre " ))
d={}
for i in range (1 , n + 1):
    d[i]=i*i

print(d)

 #Question5   

    
list= [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]

list_trier=sorted(list, key=lambda x: x[1], reverse=True)

print(list_trier)"""

sets={0,1,2,3,4}
for x in sets:
    x+=1
    print(x)
sets.add(7)
sets.remove(1)
print(sets)









