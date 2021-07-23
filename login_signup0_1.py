import FileOperation0_3 as FO, Encoder as EC

def dataUpdate(Id, Bank):
    F = open("dataF.txt", "r+")
    strF = F.read()
    begin = strF.index(Id) + 1
    end = strF.index(Id) + 5
    data = strF[begin:end]
    Index = strF.index(Bank) + 10
    F.seek(Index + 10)


def AccountInitiallize(Id, Bank, key):
    Id = "\n" + Id + " \n"
    Bank = "Bank Account " + Bank + " " + "\n"
    Amount = "Ammount : " + input("Ammount: ") + "\n"
    SKc = "Secret Key code : " + input("Secret Key code: ") + "\n"
    Address = "Adress : " + input("Address: ") + "\n"
    data = Id + Bank + Amount + SKc + Address
    #     Id=ceaserCipher_arr(data, key)
    F = open("dataF.txt", "a")
    F.write(data)
    F.close()
    F = open("dataF.txt", "r+")


def login(un, password, un_arr):
    key = EC.keyGen_string(password)
    encrypted_uni = EC.ceaserCipher(un, key)
    return encrypted_uni in un_arr


def signup(un, password, un_arr):
    key = EC.keyGen_string(password)
    encrypted_uni = EC.ceaserCipher(un, key)
    return not encrypted_uni in un_arr

##############MAIN################
