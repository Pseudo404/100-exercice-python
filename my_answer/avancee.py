"""
REVISER LES :
    - niv 75 (revoir le systeme de recursivité)
                            ^^^^^^^^^^^^^^^^^^^^^^^  recusivité mutuelle ou croisé
    - niv 78
    - niv 82
    - niv 85
    - niv 87
    - niv 88
    - niv 89
"""

# # niv 75
# def nbrPaire(N):
#     if N == 1:
#         return False
#     return nbrImpaire(N-1)
# def nbrImpaire(N):
#     if N == 1:
#         return True
#     return nbrPaire(N-1)
# print(nbrPaire(5))
# print(nbrImpaire(7))

# # niv 76
# def join(L, caractere):
#     ch = ''
#     for i in range(len(L)):
#         ch = ch + caractere + str(L[i])
#     return ch
# print(join(["tu", "vas", "comment", "?"]," "))

# # niv 77
# def remplacer(ch, old_word, new_word):
#     ch = ch.split(" ")
#     for i in range(len(ch)):
#         if ch[i] == old_word:
#             ch[i] = new_word
#     ch = " ".join(ch)
#     return ch
# print(remplacer("Bonjour Aurélie", "Aurélie", "Mathilde"))
# print(remplacer("j'ai 50 ans", "50", "16"))

# # niv 78
# def split(ch, caractere):
#     phrase_liste = []
#     mot_tmp = ""
#     if caractere in ch:
#         for i in range(len(ch)):
#             if ch[i] != caractere:
#                 mot_tmp += ch[i]
#                 if i == len(ch)-1:
#                     phrase_liste += [mot_tmp]
#             else:
#                 phrase_liste += [mot_tmp]
#                 mot_tmp = ""
#         return phrase_liste
#     else:
#         phrase_liste += [ch]
#         return phrase_liste
# print(split("Bonjour Aurélie", " "))
# print(split("Salut, ça va ?", ","))

# # niv 79
# def isdigit(ch):                      # or def isdigit(ch):
#     ch = ch.isnumeric()               # or    nombres = ['0','1','2','3','4','5','6','7','8','9']
#     return ch                         # or    for i in ch:
# print(isdigit("125920"))              # or        if c not in nombres:
# print(isdigit("edgte9be"))            # or            return False
#                                       # or     return True

# # niv 80
# def estUnPalindrome(nbr):
#     nbr = str(nbr)
#     nbr_inversed = nbr[::-1]
#     if nbr == nbr_inversed:
#         return True
#     return False
# print(estUnPalindrome("69596"))
# print(estUnPalindrome("4231324"))
# print(estUnPalindrome("312"))

# # niv 81
# def estUnPalindrome(nbr):
#     nbr = str(nbr)
#     nbr_inversed = nbr[::-1]
#     if nbr == nbr_inversed:
#         return True
#     return False
# liste_palindrome = []
# for i in range(100,1000):
#     for j in range(100,1000):
#         nbr = i*j
#         if estUnPalindrome(nbr):
#             liste_palindrome.append(nbr)
# print(max(liste_palindrome))

# # niv 82
# import math
# def estPremier(nbr):
#     diviseur = 2
#     while diviseur <= math.sqrt(nbr):
#         if nbr%diviseur == 0:
#             return False
#         diviseur += 1
#     return True
# def testCirculairePremier(nbr):
#     nbr_circulaire = []
#     nbr = str(nbr)
#     for i in range(len(nbr)):
#         nbr_circulaire.append(nbr[i:] + nbr[:i])
#     premier_circulaire = True
#     for nbr in nbr_circulaire:
#         nbr = int(nbr)
#         if not estPremier(nbr):
#             premier_circulaire = False
#         return premier_circulaire
# print(testCirculairePremier(9377))
# print(testCirculairePremier(36))

# # niv 83
# def estDistenct(nb):
#     nb = str(nb)
#     nb = list(nb)
#     for i in range(len(nb)-1):
#         nb.sort()
#         if nb[i] == nb[i+1]:
#             return False
#     return True
# print(estDistenct(9647))
# print(estDistenct(1343))

# # niv 84
# def codeSomme(nb):
#     if nb >= 100:
#         somme = int(nb)
#         nb_str = str(nb)
#         while somme < 1 or somme > 9:
#             somme_str = str(somme)
#             somme_list = list(somme_str)
#             somme = 0
#             for i in somme_list:
#                 somme += int(i)
#         return str(somme) + nb_str
# print(codeSomme(69810))
# print(codeSomme(3201))

# # niv 85
# def rechercheDichotomique(L, nbr):
#     sorted(L)
#     while L:
#         moitier = len(L)//2
#         if L[moitier] == nbr:
#             return True
#         elif nbr < L[moitier]:
#             L = L[:moitier]
#         else:
#             L = L[moitier+1:]
#     return False
# print(rechercheDichotomique([6, 9, 15, 36, 41, 43, 47], 41))
# print(rechercheDichotomique([-9, -1, 3, 4, 7, 11], 0))

# # niv 86
# for x in range(1, 1000):
#     for y in range(x+1, 1000):
#         for z in range(y+1, 1000):
#                 if x**2+y**2 == z**2:
#                     if x+y+z == 1000:
#                         print(x, y, z, x+y+z)

# # niv 87
# import os
# def traitementFichier(path):
#     fichier = open((path), 'r')
#     contenu = fichier.read()
#     file = open("niv87.txt", "w") 
#     contenu = contenu.split("\n")
#     print(contenu)
#     file.writelines(contenu)
#     file.close()
#     pass
# print(traitementFichier(r'niv66.txt'))

# # niv 88
# def triCroissant(L):
#     for i in range(len(L)):
#         for j in range(len(L)):
#             if L[i] < L[j]:
#                 L[i], L[j] = L[j], L[i]
#     return L
# print(triCroissant([6,1,9,-6,1,8,7]))
# print(triCroissant([-3,5.3,2,7,1,2.3,9.5]))

# # niv 89
# class Personne:
#     def __init__(self, taille, poids, age):
#         self.taille = taille
#         self.poids = poids
#         self.age = age
#     def imc(self):
#         return self.poids/(self.taille**2)
#     def imcInterPretation(self):
#         if self.imc() <= 18.5:
#             return "La personne est en insuffisance de poids"
#         elif self.imc() >= 30:
#             return "La personne est obèse"
#         else:
#             return "La personne est de corpulence normal ou en surpoids"
# julien = Personne(1.87, 95, 26)
# print(julien.imc())
# print(julien.imcInterPretation())