import threading
import sys
import hashlib



SENHAS = []

try:
    with open("password_wordlist.txt", "r") as arquivo:
        SENHAS = arquivo.read().splitlines()
except Exception as error:
    print(error)
   
def get_password():
    while True:
        try:
            senha = SENHAS.pop().encode()
            try:
                hash = hashlib.md5(senha).hexdigest()
                if compare == hash:
                    print("{} -------- [ + ]".format(senha.decode()))
                else:
                    pass             
                
            except Exception as error:
                print(error)
        except:
            break


if __name__ == "__main__":
    args = sys.argv
    compare = sys.argv[1]

    THREADS = []
    for i in range (50):
        t = threading.Thread(target=get_password)
        THREADS.append(t)

    for t in THREADS:
        t.start()
        

    for t in THREADS:
        t.join()