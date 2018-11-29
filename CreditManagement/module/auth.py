from .connection import Connection

con = Connection()

def isLoginValid(email, password):
    users = con.getUserData()

    for i in range(0, len(users)):
        print(users[i])
        if email == users[i][0] and password == users[i][1]:
            return {
                'response': True,
                'access': users[i][3],
                'id': users[i][2]
            }
    return {
        'response': False
    }
