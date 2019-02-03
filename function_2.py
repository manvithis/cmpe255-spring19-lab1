users =[
    { "id":0, "name": "Hero" },
    { "id":1, "name": "Dunn" },
    { "id":2, "name": "Sue" },
    { "id":3, "name": "Chi" },
    { "id":4, "name": "Thor" },
    { "id":5, "name": "Clive" },
    { "id":6, "name": "Hicks" },
    { "id":7, "name": "Devin" },
    { "id":8, "name": "Kate" },
    { "id":9, "name": "Klein" }    
]

friendship = [
    (0, 1),
    (0, 2),
    (1, 2),
    (1, 3),
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 6),
    (6, 7),
    (6, 8),
    (7, 8),
    (8, 9)
]
def sort_by_num_friends():
    '''README.md
    Sort from "most friends" to "least friends"
   '''
b={}
for i in users:
    count=0  
    for x in friendship:  
        if(x[0] == i['id'] or x[1] == i['id']):             #checking the number of times the id occurs in 0&1st place in friendship tuple 
            count = count + 1 
            b[i['name']]=count
for a in sorted(b, key=b.get, reverse=True): 
    print(a, b[a])
    pass
