# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character("sasuke")
define e = Character("eli")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene cn 1

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # These display lines of dialogue.

    show ssk

    s 'Oih, meu nome é Sasuke Uchiha'

    s 'Seja bem vinda a minha aldeia onde podemos desfrutar das coisas boas!' 

    hide ssk

    show eli

    e "Oih Sasuke, eu sou a elizabeth mas pode me chamar de eli"

    e "Muito obrigada por me receber tão bem aqui nesta vila"

    hide eli

    show ssk

    s "Quer conhecer minha casa?"

    hide ssk

    show eli

    e "Claro, porque não!"

    with dissolve
    scene cn 2

    hide eli
    hide ssk

    show ssk
    show eli at right

#raxitégui aqui começa o menu

    s "você quer isso?"

menu:

    "Não, sou casada!":
        jump choco1

    "sim, sasuke":
        jump choco2

label choco1:

    s "Tudo bem eu entendo... bom ja que nao quer eu não posso fazer nada, mais você não sabe oque perdeu"

    jump ssk

label choco2:

    s "Pode entrar então sinta-se em casa, pode fazer oq quiser!"

    s "Comigo também!..."

    hide ssk

    scene cn 1

    show eli

    e "obrigado pela noite passada foi ótima, talvez possamos nos ver de novo"

    hide eli

    show ssk

    s "claro eu adoraria"

    jump ssk

label ssk:

    show eli at right
    
    "fim ;)"

    # This ends the game.

    return
