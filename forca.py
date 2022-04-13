def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Forca!")
    print("*********************************")

    palavra_secreta = "banana"

    enforcou = False
    acertou = False

    while(not enforcou and not acertou):

        chute =input("Qual a letra? ")

        for letra in palavra_secreta:
            if(chute == letra):
                print(chute)


        print("jogando")




    print("Fim do jogo")

if (__name__ == "__main__"):
    jogar()