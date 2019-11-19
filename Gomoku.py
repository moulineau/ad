import math
def Grille_depart () : #initialise la grille de depart
    T = [[0] * 15 for compteur in range(15)]
    return T

int a =6552252
def afficheGrille(table): #affiche une grille
    print("\t  1   2   3   4   5   6   7   8   9   10  11  12  13  14  15")
    print("\t-------------------------------------------------------------")
    i = 65
    for ligne in table:
        string_ligne = chr(i) + "\t| "
        for colonne in ligne:
            if colonne == 0:
                string_ligne += "  | "
            elif colonne == 1:
                string_ligne += "X | "
            elif colonne == 2:
                string_ligne += "O | "
        print(string_ligne)
        print("\t-------------------------------------------------------------")
        i += 1
    return



def Jouer2(s, profondeur): #modelise le tour de l'ordinateur
    max_val = -1 * math.inf
    val = 0
    meilleure_actioni=0
    meilleure_actionj=0
    for i in range(0,15):
        for j in range (0,15):
            if(s[i][j]==0):
                s[i][j]=1

                val = Min(s, profondeur, -100000, 100000)
                if val > max_val:
                    max_val = val
                    meilleure_actioni=i
                    meilleure_actionj=j
                s[i][j]=0
    s[meilleure_actioni][meilleure_actionj]=1
    return s


def Jouer(s, profondeur):  # modelise le tour de l'ordinateur
    max = -100000  # pour modeliser -infini
    val = 0
    maxi = 0
    maxj = 0
    for i in range(0, 15):
        for j in range(0, 15):
            if (s[i][j] == 0):
                s[i][j] = 1
                val = Min(s, profondeur, -1 * math.inf, math.inf)

                if (val > max):
                    max = val
                    maxi = i
                    maxj = j
                s[i][j] = 0
    s[maxi][maxj] = 1
    return s


def Alignement_pions(s, j1, j2, n): #trouver si des combinaisons sont faites
        j1=0
        j2=0
        compteur=0
        compteurbis=0
        for i in range (0,15):
            # test sur une ligne
            for j in range(0,15):
                if(s[i][j]==1):
                    compteur+=1
                    compteurbis=0
                    if(compteur==n):
                        j1+=1
                elif(s[i][j]==2):
                    compteurbis+=1
                    compteur=0
                    if(compteurbis==n):
                        j2+=1
            compteur=0
            compteurbis=0
            #test sur un colonne
            for j in range(0,15):
                if(s[j][i]==1):
                    compteur+=1
                    compteurbis=0
                    if(compteur==n):
                        j1+=1
                elif(s[j][i]==2):
                    compteurbis+=1
                    compteur=0
                    if(compteurbis==n):
                        j2+=1
        #test sur les diagnonales
        compteur = 0
        compteurbis = 0
        for i in range (0,15):
            if(s[i][i]==1):
                compteur+=1
                compteurbis=0
                if(compteur==n):
                    j1+=1
            elif(s[i][i]==2):
                compteurbis+=1
                compteur=0
                if (compteurbis==n):
                    j2+=1
        compteur = 0
        compteurbis = 0
        #test sur les diagonales en montant
        for i in range(0,15):
            if(s[i][2-i]==1):
                compteur+=1
                compteurbis=0
                if(compteur==n):
                    j1+=1
            elif(s[i][j]==2):
                compteurbis+=1
                compteur=0
                if(compteurbis==n):
                    j2+=1


def Agagne(table,joueur): # test si nous avons un gagnant


    return False


def TerminalTest(s): # savoir si on continue le jeu ou pas
        j1=0
        j2=0
        Alignement_pions(s,j1,j2,3)
        if(Agagne(s,1)):
            return 1
        elif(Agagne(s,2)):
            return 2
        else :
            for i in range (0,3):
                for j in range (0,3):
                    if(s[i][j]==0):
                        return 0




def Eval(s):
        nb_pions=0
        gagnant=TerminalTest(s)
        for i in range (0,3):
            for j in range (0,3):
                if(s[i][j]!=0):
                    nb_pions+=1
        if(gagnant!=0):
            if(gagnant == 1 ):
                return 1000-nb_pions
            elif(gagnant ==2):
                return -1000 + nb_pions
            else :
                return 0
        j1=0
        j2=0
        Alignement_pions(s,j1,j2,3)# on choisir 2 pour n afin de connaitre les combinaisons de 2 pions
        return j1-j2

def Min(s, profondeur,alpha, beta):
        if(profondeur==0 or TerminalTest(s)!=0):
            return Eval(s)
        mini = 10000 #pour modéliser l'infini
        val=0
        for i in range (0,15):
            for j in range (0,15):
                if(s[i][j]==0):
                    s[i][j]=1
                    val=Max(s,profondeur-1,alpha, beta)
                    if(val<mini):
                        mini=val
                    s[i][j] = 0
                    if mini <= alpha:
                        return mini
                    beta = min(beta, mini)
                return mini

                s[i][j]=0
        return mini


def Max(s, profondeur, alpha, beta):
        if(profondeur == 0 or TerminalTest(s)!=0):
            return Eval(s)
        maxi= -10000 # pour modéliser l'infini
        for i in range (0,3):
            for j in range (0,3):
                if(s[i][j]==0):
                    s[i][j]=1
                    val=Min(s,profondeur-1,alpha,beta)
                    if(val>maxi):
                        maxi=val
                    s[i][j]=0
                    if (maxi>beta):
                        return maxi
                    alpha = max(alpha, maxi)
        return maxi


def action_manuelle(table,num_joueur):
    string = input("veuillez entrer la case vide à remplir sous le format : ligne(lettre)colonne(chiffre) (ex:A0)\n")
    formatation = False
    while not formatation:
        if len(string) > 3 or len(string) < 2:
            string = input(
                "veuillez entrer la case vide à remplir sous le format : ligne(lettre)colonne(chiffre) (ex:A0)\n")
        else:
            formatation = True
    if len(string) == 3:
        cellule = [ord(string[0]) - 65, int(string[2]) - 1 + 10]
    if len(string) == 2:
        cellule = [ord(string[0]) - 65, int(string[1]) - 1]
    while table[cellule[0]][cellule[1]] != 0 or not formatation:
        string = input(
            "veuillez entrer la case vide à remplir sous le format : ligne(lettre)colonne(chiffre) (ex:A0)\n")
        while not formatation:
            if len(string) > 3 or len(string) < 2:
                string = input(
                    "veuillez entrer la case vide à remplir sous le format : ligne(lettre)colonne(chiffre) (ex:A0)\n")
            else:
                formatation = True
        if len(string) == 3:
            cellule = [ord(string[0]) - 65, int(string[2]) + 10]
        if len(string) == 2:
            cellule = [ord(string[0]) - 65, int(string[1])]

    table[int(cellule[0])][int(cellule[1])] = num_joueur
    return table

if __name__ == '__main__':
        Table = Grille_depart()
        print(TerminalTest(Table))
        afficheGrille(Table)
        reponse = input("voulez vous commencer ? si vous repondez autre chose que oui l'IA commencera\n")
        IA_Turn = True
        turn = 1
        if reponse == "oui":
            Table[7][7] = 2
            afficheGrille(Table)
            Table = Jouer(Table,turn+1)
            IA_Turn = False
            afficheGrille(Table)
        else:
            Table[7][7] = 1
            afficheGrille(Table)
            Table = action_manuelle(Table, 2)
            afficheGrille(Table)
            Table = Jouer(Table,turn+1)
            IA_Turn = False
            afficheGrille(Table)

        while TerminalTest(Table)==0:
            if IA_Turn:
                Table = Jouer(Table,turn+1)
                IA_Turn = False
                afficheGrille(Table)
            else:
                Table = action_manuelle(Table, turn+1)
                IA_Turn = True
                afficheGrille(Table)
        (gagnant) = TerminalTest(Table)
        if gagnant == 0:
            "personne n'a gagné :("
        elif gagnant == 1:
            "l'IA vous a vaincu"
        elif gagnant == 2:
            "vous avez gagné !"
        affichage_grille(Table)







