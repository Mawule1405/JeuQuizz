import fonctions
import scores
import donnees

questions = donnees.question
reponses =donnees.reponse
Freponse_1 =donnees.Xreponse_1
Freponse_2 =donnees.Xreponse_2
Freponse_3 =donnees.Xreponse_3


print("Bienvenu à la  découverte du jeu Quizz pour booster votre culture")
while True:
    #connaissance du statut de chaque joueur: le nom
    while True:
        choix = input("Etes vous un nouveau joueur (Y/N)").upper()
        if choix == 'Y': #Si il est nouveau il s'enregistre
            nom = fonctions.enregistrement_joueur()
            break
        elif choix == 'N': #Si il est ancien
            while True:
                nom = input('Veillez entrer votre nom: ').upper() #vérification de l'identité d'un ancien joueur
                validation = fonctions.recherche_joueur(nom)
                if validation == False:
                    print("Désolé ce nom n'est pas dans nos achives! Si vous êtes vréaaiment un ancien veillez corriger le nom")
                else:
                    print("Bonne chance pour le jeu!")
                    break
        else:
            print("Mauvais réponse")
        if validation:
            break
    #lancement de la partie
    numero = 1
    while True:
        print(f"Début du jeu! Nom du joueur: {nom}")
        print(f"              Ancien score {scores.dict_scores[nom]}  ")
        print("                     ")
        
       
        print(f"Question: {questions[str(numero)]}")
        choix = input(f""" 
                    Choisissez la lettre correspondante à la bonne réponse:
                    a : {Freponse_1[str(numero)]}
                    b : {reponses[str(numero)]}
                    c : {Freponse_2[str(numero)]}
                    d : {Freponse_3[str(numero)]}
              
              """).lower()
        if  choix == "a":
            reponse_joueur  = Freponse_1[str(numero)]
        elif choix == "b":
            reponse_joueur = reponses[str(numero)]
        elif choix == 'c':
            reponse_joueur = reponse_2[str(numero)]
        elif choix == 'd' :
            reponse_joueur = Freponse_3[str(numero)]
        else :
            point = -2
            
        if reponse_joueur == reponses[str(numero)]:
            point = 10
            print(f"Bonne réponse +{point}")
        elif point == -2:
            print(f"Maivais choix! Pénalité {point}")
        else:
            point = -5
            print(f"Mauvaise réponse {point}")
        
        fonctions.enregistrement_scores(nom, point)   
        #Demande de permission de continuer le jeu
        choix = input(' Souhaitez vous continuer ? (Y/N)  ')
        if choix == "N":
            break
        else: 
            numero +=1
            if numero > len(questions):
                break
    if choix == 'N' or numero > len(questions):
        break
           

    