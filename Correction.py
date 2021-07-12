direction=input("Voulez-vous allez à gauche ou à droite ? (gauche/droite) : ")

if direction=='gauche':
    dommages=int(input("Vous attaquez un Troll"))
    if dommages>10 :
        print("Vous avez gagné")
    elif 0 <= dommages<= 10 :
        print("Vous avez perdu")
    else:
        print("valeur invalide")
elif direction=='droite':
    reponse=input("Est-ce qu'une pieuvre à 3 coeurs ? (oui/non) :")
    if reponse=='oui':
        reponse=True
    elif reponse=='non':
            reponse=False
    else:
        print("Valeur invalide")
    if reponse==True:
        print('Vous avez gagné')
    else:
        print('Vous avez perdu.')
else:
    print('Vous avez rentré une mauvaise valeur')

