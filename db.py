from werkzeug.security import generate_password_hash, check_password_hash
import json

class Database:

    def insert(self,name,email,password):
        with open('users.json','r') as rf:
            users = json.load(rf)

            if email in users:
                return 0
            else:
                hashed_password = generate_password_hash(password)
                users[email] = [name,hashed_password]

        with open('users.json','w') as wf:
            json.dump(users,wf,indent=4)
            return 1

    def search(self,email,password):
        with open('users.json','r') as rf:
            users = json.load(rf)

            if email in users:
                stored_hash = users[email][1]
                if check_password_hash(stored_hash, password):
                    return 1
                else:
                    return 0
            else:
                return 0
