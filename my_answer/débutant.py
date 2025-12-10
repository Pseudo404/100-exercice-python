# #niv 1
# a, b, c = 1, "France", 36.2
# print(a, b, c)

# #niv 2
# ch = "salut"
# ch = "ça va"
# print(ch)

# #niv 3
# x, y = 3, 8.5
# print(type(str(x)), type(str(y)))

#niv 4
# poids = int(input("quel est ton poids ? "))
# print(poids)

# #niv 5
# var = "Bonjour"
# if type(var) is str: # is or == but 'is' is better
#     print("chaine de caractères")
# elif type(var) is int:
#     print("Entier")

# #niv 6
# d = 5
# if d >= 0:
#     print("Positive")
# else :
#     print("Negative")

# #niv 7
# age = int(input("quel est ton age ? "))
# if age >= 18:
#     print("l'utilisateur est majeur")
# else:
#     print("l'utilisateur est mineur")

# #niv 8
# for i in range(1, 21):
#     print(i)
# j = 1
# while j < 21:
#     print(j)
#     j += 1

# # niv 9
# for i in range(10, 21):
#     if i%2:
#         print(i)
# j = 0
# while j > 21:
#     j += 1
#     if j%2:
#         print(j)

# # niv 10
# liste = [i for i in range(1, 11)]
# print(liste)

# # niv 11
# liste = [i for i in range(1, 11) if i%2 == 0]
# print(liste)

# # niv 12
# L = [6,8,3,4,1,12,2,9.2]
# L.sort()
# print(L)

# # niv 13
# L = [3,2,2,1,9,1,2,3,7]
# print(L.count(1))

# # niv 14
# L = []
# L += 10,25,30,45,90,'ab','cd','ef'
# print(L)

# #niv 15
# L = [1,2,3,4,5,6,7,8,9,10]
# L1 = []
# for i in range(len(L)):
#     if i%3 == 0:
#         L1.append(L[i])
# print(L1)

# #niv 16
# c = 'france'
# c = sorted(c)
# c = "".join(c)
# print(c)

# #niv 17                                   
# L1 = [9,8,7,14,3,2,'a','p','bonjour','b']
# L2 = ['b',1,9.2,6,3,9,'p']
# L3 = set(L2).intersection(set(L1))
# L3 = list(L3)
# print(L3)

# # niv 18
# L = [("Pomme", 15),("Banane", 8), ("Fraise", 12), ("Kiwi", 9), ("Peche", 2)]
# L.sort(key = lambda x : x[1])
# print(L)

# # niv 19
# ch = "Bonjour tout le monde"
# ch_inversed = ch[::-1]
# print(ch_inversed)

# # niv 20
# d = {"Pomme":3, "Banane":7, "Kiwi":1}
# print(d["Pomme"], d["Banane"])

# # niv 21
# di = {"Pomme":15,"Banane":8, "Fraise":12, "Kiwi":9, "Peche":2}
# somme = sum(di.values())
# print(somme)

# # niv 22
# a = 187.632587
# a = float("{:.2f}".format(a))
# print(a)

# # niv 23
# monNom = 'Julien'
# age = 32
# langage = 'Python'
# ch = f"Je m'appelle {monNom} et j'ai {age} ans. J'apprends le langage {langage}".format(monNom, age, langage)
# print(ch)

# # niv 24
# for i in range(11):
#     print("8x", i, "=", i*8)

# # niv 25
# import os
# print(os.getcwd())

# # niv 26
# L = [1,2,3,4,5]
# L.remove(1)
# print(L)

# # niv 27
# import os
# path = r"C:\Users\cizea\'niv 1.py'"
# nom_fichier = os.path.basename(path)
# extend_fichier = nom_fichier.split(".")[-1]
# print("extension du fichier est :", extend_fichier)

# # niv 28
# import time
# start_time = time.time()
# for i in range(11):
#     print("8x", i, "=", i*8)
# end_time = time.time()
# ellapsed_time = end_time - start_time
# print(ellapsed_time)

# # niv 29
# import random
# L = [3,6,8,7,2, "s", "ch", "d"]
# random.shuffle(L)
# print(L)

# # niv 30
# import random
# alea = random.randint(20,30)
# print(alea)

# # niv 31
# liste = [i for i in range(5, 21)]
# for loop in range(8):
#     print(liste)

# # niv 32                              or                  L = [3,6,9,12,15,18,21,24]       
# L = [3,6,9,12,15,18,21,24]            or                  L1 = [l/3 for l in L]
# L1 = []                               or                  print(L1)
# for i in range(len(L)):
#     L1.append(L[i]/3)
# print(L1)

# # niv 33
# L = [-6,5,-3,-1,2,8,-3.6]
# L1 = [l for l in L if l>0]
# print(L1)