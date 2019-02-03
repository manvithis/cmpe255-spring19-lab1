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

def num_friends(user):
    '''
    Find number of friends for a given user
    '''
    uid=0
    count=0  
    for i in users:
        if i["name"] == user:            #checking is the user is present in users
            print("user present")
            uid=i["id"]                  #taking the users id
            break
        else:
            uid=9999
            
    if uid==9999:                        #checking if the user entered correct user name
        print("please enter correct user")
    else:
        for x in friendship:              
            if (x[0] == uid):             #checking the number of times the id occurs in 0th place in friendship tuple
                count = count + 1 
        print("The number of friends for %s is %s"%(user, count)) 

        
        
        
num_friends("Chi") 