def users(CorrectUsers, AllCurrentUsers):
    BadUsers = []
    CorrectUsers = CorrectUsers.split(",")
    AllCurrentUsers = AllCurrentUsers.split(",")
    for i in CorrectUsers:
        CorrectUsers[CorrectUsers.index(i)] = CorrectUsers[CorrectUsers.index(i)].replace(" ", "")
    for i in AllCurrentUsers:
        AllCurrentUsers[AllCurrentUsers.index(i)] = AllCurrentUsers[AllCurrentUsers.index(i)].replace(" ", "")
    CorrectUsers = set(CorrectUsers)
    AllCurrentUsers = set(AllCurrentUsers)
    x = AllCurrentUsers.difference(CorrectUsers)
    print(x)
    
    
users("Basu, John, Jimmy","Basu, John, Sauron,Jimmy, Kali")