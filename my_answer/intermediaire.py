"""
REVISER LES :
    - import os
    - niv 49
    - niv 54
    - niv 60
    - niv 65
    - niv 67
    - niv 72
    - niv 73
    - niv 74
"""

# # niv 34
# def f(a, b, x):
#     result = a*(x**3)+2*a*(x**2)+b
#     return result
# print(f(3,0,1))
# print(f(0,2,2))

# # niv 35
# def VerfiPresence(num, L):
#     for i in range(len(L)):
#         if i == num:
#             return True
#     return False
# print(VerfiPresence(2,[1,2,3,4,5,6]))
# print(VerfiPresence(-1,[3,6,9,7,"abcr"]))

# # niv 36
# a = 3018
# a = str(a)
# somme = 0
# for chiffre in a:
#     somme += int(chiffre)
# print(somme)

# # niv 37
# def calculSomme(L):
#     somme = 0
#     for i in range(len(L)):
#         somme += L[i]
#     return somme
# print(calculSomme([3,2,6,9,-1,5]))
# print(calculSomme([-3,-6,0,1,2,7]))

# # niv 38
# def supprimeDoublons(L):                                # or L = [0,3,5,7,3,5,1,-1]
#     L.sort()                                            # or L = set(L)       Supprime les doublons ici
#     for i in range(len(L)):                             # or L = list(L)
#         doublons = L.count(i)                           # or print(L)
#         if doublons >= 2:                               # or 
#             for j in range(doublons-1):                 # or 
#                 L.remove(i)                             # or 
#     return L                                            # or 
# print(supprimeDoublons([0,3,5,7,3,5,1,-1]))             # or 
# print(supprimeDoublons([0,5,9,10,3.21,-3]))             # or 

# # niv 39
# def ajoutElementDict(cle, valeur, dico):
#     dico[cle] = valeur
#     return dico
# print(ajoutElementDict('a', 1, {'b':2}))
# print(ajoutElementDict('a', 1, {}))

# # niv 40
# def maxi(L):                           # or maximum = L[0]
#     L.sort()                           # or for i in L:
#     maximum = L[len(L)-1]              # or if i > maximum:
#     return maximum                     # or     maximum = i
# print(maxi([-9,2,4,1,8]))              # or return maximum
# print(maxi([-3,1,7,6,2,3]))            # or print(maximum([-9,2,4,1,8]))

# # niv 41
# def sommeSousListe(L, i, j):
#     lij = L[i:j+1]
#     somme = 0
#     for k in lij:
#         somme += k
#     return somme
# print(sommeSousListe([4,10,12,16,18], 2, 4))
# print(sommeSousListe([2,4,6,8,10,12], 0, 2))

# # niv 42
# for i in range(1, 7):
#     print('*'*i, "\n")

# # niv 43
# def mini(L):
#     L.sort()
#     return L[0]
# print(mini([-9,2,4,1,8]))
# print(mini([-3,1,7,6,2,3]))

# # niv 44
# def longueur(L):
#     lenght = 0
#     for i in L:
#         lenght += 1
#     return lenght
        
# print(longueur([3,6,7,'abcde', [1,3,57], True]))
# print(longueur([]))

# # niv 45
# def moyenne(L):
#     somme = sum(L)
#     moyenne = somme / len(L)
#     return moyenne
# print(moyenne([1,2,3,4,5,6,7]))
# print(moyenne([3,0,-1,5,6,9,17]))

# # niv 46
# def diviseur(n):
#     L = []
#     for div in range(1, n+1):
#         if n % div == 0:
#             L.append(div)
#         L.sort()
#     return L
# print(diviseur(3))
# print(diviseur(9))

# # niv 47
# def verifMaj(ch):
#     if ch.islower() == True:
#         return False
#     else:
#         return True
# print(verifMaj("LOL hahhha..."))
# print(verifMaj("si tu lis çà envoie un snap plz 😂"))

# # niv 48
# def concatenateListe(L1, L2, L3):
#     L = L1
#     L.extend(L2)
#     L.extend(L3)
#     return L
# print(concatenateListe([0,9,8], [2,6,9], [True, False, 'abcde']))
# print(concatenateListe([[38,-1], -3, 9], ["xz", "France"], []))

'''A REVOIR'''
# # niv 49
# def nbrValeurDict(d):
#     cle = list(d.keys())
#     valeur = 0
#     for i in cle:
#         longueur = len(d[i])
#         valeur += longueur
#     return valeur
# print(nbrValeurDict({'a':[1,2,3],'b':[3,'p'],'c':[8]}))
# print(nbrValeurDict({'Julie':[12, 60.1],'Fred':[26, 75.6],'David':[]}))

# # niv 50
# def concatDict(d1, d2):
#     d = {}
#     d.update(d1)
#     d.update(d2)
#     return d
# print(concatDict({'a':3, 'b':6}, {'c':2, 'd':-1}))
# print(concatDict({'d':[2.9, 4.1]}, {'p':[]}))

# # niv 51
# import math
# def calculFactorielle(n):
#     n = math.factorial(n)
#     return n
# print(calculFactorielle(3))
# print(calculFactorielle(9))
# print(calculFactorielle(0))

# # niv 52
# def diviseursMult(n, a, nbrSeuil):
#     L = []
#     for i in range(n, nbrSeuil):
#         if i % n == 0 and i % a != 0:
#             L.append(i)
#     return L
# print(diviseursMult(5, 2, 100))
# print(diviseursMult(11, 3, 85))

# # niv 53
# def presenceVoyelle(ch):
#     for i in ch:
#         if i == 'a' or i == 'e'or i == 'i' or i == 'o' or i == 'i' or i == 'u' or i == 'y':
#             return True
#     return False
# print(presenceVoyelle("ne t'inquiete pas !"))
# print(presenceVoyelle("vcwx"))

"""A REVOIR"""
# # niv 54
# def supprEspace(ch):
#     ch = ch.split(" ")
#     ch = "".join(ch)
#     return ch
# print(supprEspace("Ne t'inquiete pas !"))
# print(supprEspace("je me casse"))

# # niv 55
# def positionXListe(L, x):
#     xListe = []
#     for i in range(len(L)): # [1,2,4,5,6,7,3,9,3]
#         if L[i] == x: #                    ^   ^ i = 6, 8
#             xListe.append(i) # xliste = [6, 8]
#         if L.count(x) == 0:
#             return f'cette liste ne contient pas de {x}'.format(x)
#     return xListe
# print(positionXListe([1,2,4,5,6,7,3,9,3], 3))
# print(positionXListe([1,2,4,5,6,7,3,9,3], -3))

# # niv 56
# def filtrerMots(ch, min):
#     ch = ch.split()
#     filtre = []
#     for i in ch:
#         if len(i) >= min:
#             filtre.append(i)
#     filtre = " ".join(filtre)
#     return filtre
# print(filtrerMots("ok tout va bien se passer tranquille !", 5))

# # niv 57
# def inversPhrase(ch):
#     ch = ch.split()
#     ch.reverse()
#     ch = " ".join(ch)
#     return ch
# print(inversPhrase("Comment vas tu ?"))

# # niv 58
# def nombreOccurence(L):
#     Occu = []
#     for i in range(len(L)):
#         if Occu.count(L[i]) == 0:
#             Occu.append((L[i], L.count(L[i])))
#     Occu = set(Occu)
#     Occu = list(Occu)
#     return Occu
# print(nombreOccurence([-4,8,-3,2,1,2,7,9,-3,8,1]))
# print(nombreOccurence(["a", 3, 4, "b", "a", 3]))

# # niv 59
# def unionListe(L1, L2, L3):
#     L = []
#     L.extend(L1)
#     L.extend(L2)
#     L.extend(L3)
#     L = set(L)
#     L = list(L)
#     L.sort()
#     return L
# print(unionListe([3,6,9,3],[1,0,3],[12,6,0]))
# print(unionListe([7,44,-3],[],[7,2,7]))

# # niv 60
# def calculPGCD(a, b):
#     assert(a>0 and b>0)
#     while b != 0:
#         a, b = b, a%b
#     return a
# print(calculPGCD(3,5))
# print(calculPGCD(5,15))

# # niv 61
# import os
# def lireFichier(path):
#     fichier = open(path, 'r')
#     contenu = fichier.read()
#     return contenu
# print(lireFichier(r"C:\Users\cizea\Desktop\defi\niv61.txt"))

# # niv 62
# import os
# def nbrOccFichier(path, word):
#     nb = 0
#     fichier = open(path, 'r')
#     contenu = fichier.read()
#     contenu = str(contenu)
#     contenu = contenu.split(" ")
#     for i in contenu:
#         if i == word:
#             nb += 1
#     return f"le mot '{word}' apparait {nb}x dans le fichier"
# print(nbrOccFichier(r"C:\Users\cizea\Desktop\defi\niv62.txt", 'tkt'))

# # niv 63
# import os
# def supprCarac(path, carac):
#     fichier = open(path, 'r')
#     contenu = fichier.read()
#     contenu = str(contenu)
#     contenu = list(contenu)
#     for i in contenu:
#         if i == carac:
#             contenu.remove(',')
#     contenu = "".join(contenu)
#     return contenu
# print(supprCarac(r"C:\Users\cizea\Desktop\defi\niv63.txt", ','))

# # niv 64
# import os
# def pressenceNombre(path):
#     fichier = open(path, 'r')
#     contenu = fichier.read()
#     contenu = str(contenu)
#     for i in contenu:
#         if i.isdigit():
#             return True
#     return False
# print(pressenceNombre(r"C:\Users\cizea\Desktop\defi\niv64.txt"))

# # niv 65
# import os 
# def nbFichier(chemin):
#     nbr_file = 0
#     list_of_contenu = os.listdir(chemin)
#     for contenu in list_of_contenu:
#         if os.path.isfile(os.path.join(chemin, contenu)):
#             nbr_file += 1
#     return nbr_file
# print(nbFichier(r"C:/Users/cizea/Desktop/defi"))

# # niv 66
# import os
# def ecrireFichier(path, text):
#     fichier = open(path, 'w')
#     contenu = fichier.write(text)
#     fichier.close()
#     pass
# print(ecrireFichier(r"C:\Users\cizea\Desktop\defi\niv66.txt", "tktp j'ai ecris ca avec un fichier python !"))

# # niv 67
# def cleMaxValeurDic(d):
#     cle_val = []
#     cle = list(d.keys())
#     for i in cle:
#         val_cle = len(set(d[i]))
#         cle_val.append((i, val_cle))
#     cle_val.sort(key = lambda x : x[1])
#     cle_max_val = cle_val[-1][0]
#     return cle_max_val
# print(cleMaxValeurDic({'a' : [9,10,9,7,3], 'b' : [5,3,2,2,2], 'c' : [1,1,1,1,1,1,8,2]}))
# print(cleMaxValeurDic({'dtg' : [6, 8, 1], 'fgb' : [2.5, 'a'], 'klm' : ['p', 3, 3]}))

# # niv 68
# liste_utilisateur = input("donne une liste")
# liste_utilisateur = list(liste_utilisateur.split(' '))
# print(liste_utilisateur)

'''TOUT BON SEULMENT 2ieme FACON POSSIBLE'''
# # niv 69
# def nbrJourHeure(dateDebut, dateFin):
#     dateDebut = list(dateDebut.split("/"))
#     dateFin = list(dateFin.split("/"))
#     if int(dateFin[1]) % 2 != 0:
#         jourpasser = (int(dateFin[1])-int(dateDebut[1]))*30
#     else:
#         jourpasser = (int(dateFin[1])-int(dateDebut[1]))*31
#     jourpasser += int(dateFin[2])-int(dateDebut[2])
#     datePasser = (jourpasser, jourpasser*24)
#     return datePasser
# print(nbrJourHeure("2022/05/15","2022/06/20"))
# print(nbrJourHeure("2022/04/1","2022/04/27"))

# # niv 70
# import random
# def genereMDP(caracteres, tailleMDP):
#     MDP = []
#     for i in range(tailleMDP):
#         MDP.append(random.choice(caracteres))
#     random.shuffle(MDP)
#     MDP = "".join(MDP)
#     return MDP
# print(genereMDP('tomlefouactuellementilest5hdumatin', 30))

# # niv 71
# import math
# def fonctTrigo(x):
#     resultat = math.cos(x) * math.sin(x) + math.sin(x) + 8
#     return resultat
# print(fonctTrigo(math.pi/4))
# print(fonctTrigo(math.pi))

# # niv 72
# liste_entiers = []
# for nbr in range(100, 1000):
#     str_nbr = str(nbr)
#     somme_chiffre = int(str_nbr[0]) + int(str_nbr[1]) + int(str_nbr[2])
#     produit_chiffre = int(str_nbr[0]) * int(str_nbr[1]) * int(str_nbr[2])
#     if produit_chiffre % somme_chiffre == 0:
#         liste_entiers.append(nbr)
# print(liste_entiers)

# # niv 73
# def calculSomme(L):
#     if len(L) == 0:
#         return 0
#     return L[0] + calculSomme(L[1:])
# print(calculSomme([3,2,6,9,-1,5]))
# print(calculSomme([-3,-6,0,1,2,7]))

# # niv 74
# def suiteFibonacci(N):
#     if N <= 2:
#         return 1
#     return suiteFibonacci(N-1) + suiteFibonacci(N-2)
# print(suiteFibonacci(25))
# print(suiteFibonacci(45))