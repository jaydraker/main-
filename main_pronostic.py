from random import*               
import sys
import os
import datetime



def SaisirEquipe(liste_equipe):
    NombreEqui = input("Sur combien d'equipe allez vous parier cher parieur ?")
    int(NombreEqui)
    i = 1
    a = int(NombreEqui)
    liste_equipe = []
    for i in range(1, a+1):
        print("Equipe",i)
        NomEquipe = input()
        cote_victoire = input("Victoire: ")
        cote_2_buts_dans_le_matchs = input("2 buts dans le match: ")
        cote_1_but_en_premiere_mi_temps = input("1 but en premiere mi-temps: ")
        fichier_equipe = open('base_equipe.txt', 'a')
        line_equipe = 'Nom:{}, Victoire:{}, 2 buts dans le match:{}, 1 but en premiere mi-temps:{}\n'.format(NomEquipe,cote_victoire,cote_2_buts_dans_le_matchs,cote_1_but_en_premiere_mi_temps)

        fichier_cote_victoire = open('base_cote_victoire.txt','a')
        fichier_cote_2buts_match = open('base_cote_2buts_match.txt','a')
        fichier_cote_1but_mi_temps = open('base_cote_1but_mi_temps.txt','a')

        line_cote_victoire = '{}\n'.format(cote_victoire)
        line_cote_2buts_match = '{}\n'.format(cote_2_buts_dans_le_matchs)
        line_cote_1but_mi_temps = '{}\n'.format(cote_1_but_en_premiere_mi_temps)

        fichier_cote_victoire.write(line_cote_victoire)
        fichier_cote_2buts_match.write(line_cote_2buts_match)
        fichier_cote_1but_mi_temps.write(line_cote_1but_mi_temps)
        fichier_cote_victoire.close()
        fichier_cote_2buts_match.close()
        fichier_cote_1but_mi_temps.close()

        fichier_equipe.write(line_equipe)
        fichier_equipe.close()

    print("Les differentes equipes sont les suivantes\n")
    fichier_equipe = open('base_equipe.txt', 'r')
    os.system('cls')
    lignes = fichier_equipe.readlines()
    for ligne in lignes:
        print(ligne, end='')
    fichier_equipe.close()
   
    os.system('pause')
    menu()


def affichage_pronostic():
    print("Vous etes bien sur la partie de l'affichage")


def menu():

    
    print("                        BIENVENUE SUR PRONOSTIC DE PARIS\n\n\n\n\n")
    print("PRINCIPE \n\n")
    print("Le principe est de rentrer le nombre d'equipe puis les noms des differentes equiques,\nensuite les cotes des equipes et vous verrez affichez tous les pronostic")
    print("\n\n\n\n")
    #os.system('pause')
    print("1. Entrer les equipes")
    print("2. Affichage des combinaisons")
    print("3. Sortir")
    choix = input("Votre choix:")
    liste_equipe = []
    
    while choix != "1" and choix != "2" and choix !="3"  :
        choix= input(" Votre choix svp : ")
    if choix == "1" :
        print("Saisir les equipes")
        #os.system('pause')
        SaisirEquipe(liste_equipe)
       
    if choix == "2" :
        
        affichage_pronostic()
        os.system('pause')

    if choix == "3" :
        print("Bye Bye (-.-)")
        os.system('pause')














#LA FONCTION PRINCIPAL MAIN--------------------------------------------------------------------------------------------------------------------------


def main():
   
    
    trash=os.system('cls')
    menu()
    
    
		
if __name__== '__main__':
    main()



