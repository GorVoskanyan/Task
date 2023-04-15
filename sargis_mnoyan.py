# from math import pi

# class Covid19:
#         '''returns your symptom'''
#         def __init__(self,celsus):
#             self.celsus=celsus
#         def temperature(self):
#             if 120<pi*self.celsus<128:
#                 return "you have coronavirus"
#             else:
#                 return "all is okay"


# aram=Covid19(36.6)
# karen=Covid19(40.74)
# print(aram.temperature())
# print(karen.temperature())





# class Names:
#     def __init__(self,name):
#         self.name = name
#     def widespread(self):
#         '''checks the prevalence of your name'''
#         k=0
#         dct={1:'ajs', 2:'bkt', 3:'clu',4:'dmv', 5:'enw', 6:"fox",
#                 7:'gpy',8:"hqz", 9:"i"}
#         for i in self.name:
#             for key in dct:
#                 if i in dct[key]:
#                     k+=key
#         if k**0.5<5:
#             return f'{k}, yes'
#         else:
#             return f"{k},no"
        
# sargis=Names('sargis')
# print(sargis.widespread())





# import random

# class HarryPotter:
#     def game(self):
#         y=l=0
#         lst=['Avada Kedavra',"Crucio","Imperio"]
#         while y!=2 and l!=2:
#             lord=random.choice(lst)
#             word=input('enter word >> ')
#             print(lord)
#             if word==lord:
#                 y+=1
#             else:
#                 l+=1
#         if l>y:
#             return "you lost"
#         else:
#             return "you win!!"

        
# a=HarryPotter()
# print(a.game())