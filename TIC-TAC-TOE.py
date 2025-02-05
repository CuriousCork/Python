'''
    Programador.....: Diogo Ramiro
    Data............: 03/02/25
    Observacoes.....: Jogo do Galo TIC-TAC-TOE
'''

def presentMenu():
    print("------------------------------")
    print("Welcome to TIC-TAC-TOE")
    print("------------------------------")
    print("Option 1 - Play the game")
    print("Option 2 - Exit")
    print("------------------------------")

def receiveOption():
            option = int(input("Select an Option: "))
def handleOption(option):
    if option == 1:
        print("Starting the game...")
    elif option == 2:
        print("Exit.")
        exit()
    else:
        print("TIncorrect Option.")
        exit()

presentMenu()
option = receiveOption()  
handleOption(option)  
