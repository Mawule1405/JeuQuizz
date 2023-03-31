
"""Cette fichier contient toutes les fonctions dont on a besoin  """
import scores


#Rechche de l'exercice du joueur ou nom
def recherche_joueur(nom):
    """ Cette fonction a pour but chercher le nom d'un joueur dans la liste des jours
    Elle renvoie True si trouver et False si non"""
    dict_joueur = scores.dict_scores
    trouver = False
    for i in dict_joueur:
        if i == nom:
            trouver = True
            break
    return trouver

#Verification du nom de joueur qui ne doit ni commecer par un chiffre, ni etre vide ,
# ni contenir d'espace
def verification_nom(nom):
    """elle vérifie si un nom est valide ou pas """    
    valider = False
    if len(nom)==0:
        return valider
    elif not nom[0].isdigit(): # on vérifie si la premiere lettre est un chiffre ou non? Si non
        for j in nom: #O recherche si le nom contient ou pas de caractere vide
            if j == " ":
                valider = False
                break
            else: 
               valider = True
        return valider           
    else:
        return valider
             


def enregistrement_scores(nom, point):
    """  permet d'enregistrer le score d'un joueur """
    dict_joueur = scores.dict_scores
    for name,score in dict_joueur.items():
       if name == nom:
           score +=point
           dict_joueur[name] = score
    with open("C:/Users/hp/Desktop/Quizz/scores.py" , "w") as file:
        file.write(f"dict_scores = {dict_joueur}")
        file.close()
        
       
    
# cette fonction permet d'enregistrer un nouveau joueur joueur
def enregistrement_joueur():
    dict_joueur = scores.dict_scores
    """c'est une fonction qui permet l'enregistrement d'un nouveau joueur """
    print("Bienvenu dans le jeu de QUIZZ.")
    while True: 
        nom_joueur = input(" Veillez entrer votre nom: ").upper()
        #Controle du nom saisir
        validation_nom =verification_nom(nom_joueur) 
        if validation_nom == True:
            reponse_recherche = recherche_joueur(nom_joueur)
            if reponse_recherche == True:
                print("Désolé ce nom est déjà utilisé! veillez changer")
            else: 
                dict_joueur[nom_joueur]=0
                return nom_joueur
                break  
        else:
            print(f"Le nom {nom_joueur} est invalide") 
    "Enregistrement de ll'utilisateur dans le fichier des scores avec un score minimal de 0"
    with open("C:/Users/hp/Desktop/Quizz/scores.py", "w") as file:
        file.write(f"dict_scores = {dict_joueur}")
        file.close()    