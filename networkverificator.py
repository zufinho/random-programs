# i made this when i no have connection network lol the unique form to me warn the user when is network on is shutdowing pc and cancelling it xd
# eu fiz isso quando tava sem internet kkkk, então a unica forma que eu vi para avisar o usuario quando a internet voltasse era dando um aviso de desligamento com o comentario que a internet voltou e cancelando kkkkkkkkkkkkkkkkk
from requests import get
from os import system
from time import sleep
count=0
while True:
    try:
        get("https://google.com")
        system(f'shutdown -s -t 30 -c "After {count} attempts, Your network is ON!"')
        sleep(5)
        system("shutdown -a")
        break
    except:
        count+=1
        print(f"Failed, attempt {count}")
        