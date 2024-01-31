friends = [("shemis",20),("patrick",19),("jack",25),("candis",17),("vic",18),("linda",21)]


age = lambda data: data[1] >= 18


smokin_buddies = list(filter(age, friends))


for i in smokin_buddies:
    print(i)