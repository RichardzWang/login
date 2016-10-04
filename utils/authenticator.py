import csv, hashlib

info = 'data/passwords.csv'

def register(inusername, inpassword):
    with open(info) as csvfile:
        reader = csv.reader(csvfile)
        unlocked = dict(reader)
        for username in unlocked:
            if username == inusername:
                return False
    with open(info, "w") as csvfile:
        FieldNames = ['username','password']
        writer = csv.DictWriter(csvfile, fieldnames = FieldNames)
        hexedpass = hashlib.sha224(inpassword).hexdigest()
        writer.writerow({'username' : inusername , 'password' : hexedpass})
    return True

def authuser(inusername):
    with open(info) as csvfile:
        reader = csv.reader(csvfile)
        dictreader = dict(reader)
        for username in dictreader:
            if username == inusername:
                return True
    return False


def auth(inusername,inpassword):
    with open(info) as csvfile:
        rawreader = csv.reader(csvfile)
        reader = dict(rawreader)
        for username in reader:
            if username == inusername:
                if (hashlib.sha224(inpassword).hexdigest() == reader[username]):
                    return -1 #SUCCESSFUL
                else:
                    return -2 #PASSWORD INCORRECT
            else:
                return -3 #USERNAME INCORRECT

        
