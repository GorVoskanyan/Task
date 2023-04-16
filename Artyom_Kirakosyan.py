# import math
# class Covid:
#     '''The doctors and the scientists are found out that you can learn about your illness
# coronavirus from home by the following formula. If you duplicate your body temperature by
# Celsus with the number of pi(math) and round up to the nearest whole number and if it is
# between the intervals of 120 to 128 so you have coronavirus otherwise no.'''
    
#     def covid_test(self, temp:float)->float:
#         body_temp = temp * math.pi
#         if 128 > body_temp and  math.ceil(body_temp) >= 120:
#             print (math.pi,body_temp )
#             return 'You Have coronavirus'
#         print (math.pi,math.ceil(body_temp) )    
#         return 'Everything is ok'
        

# Artyom = Covid()
# print(Artyom.covid_test(36.6))



# class FindNameNumber():
#     '''This class  accepts a string of your name and it will tell the 
#        number of your name will tell if it is widespread or not .
#        '''
    
#     def find_name(self,name):
#         dct = {1 :'ajs', 2 : 'bkt', 3 : 'clu', 
#                4 : 'dmv',5 : 'enw', 6 : 'fox',
#                7 : 'gpy', 8 : 'hqz', 9 : 'i'}
#         accum = 0
#         for name_letter in name.lower():
#             for key, value in dct.items():
#                 if name_letter in value:
#                     accum +=key
#         if accum ** 0.5 < 5:
#             return f'{accum}, Yes'
#         return f'{accum}, No'
# Artyom = FindNameNumber()
# print(Artyom.find_name('Ani '))


# import random
# class HarryPoter:
#     '''You are Harry Potter and you fight with Lord Voldemort in order to protect your friends. 
#     You should use magic words for winning him. You both use the following magic words 
#     during fighting: Avada Kedavra, Crucio, Imperio . You get 1 point when your word 
#     corresponds to his, otherwise you lose 1 point. You have three attempts and you will 
#     become a winner if you have 2 corresponding words'''
#     def win_voldemord(Self):
#         magic_words = ("Avada Kedavra", "Crucio", "Imperio")
#         vold=''
#         print('Choise one of this magic words` Avada Kedavra, Crucio or Imperio')
#         for _ in range(3):
#             result = 0
#             word = random.choice(magic_words)
#             vold+=word+' '
#             inp = input('Enter your magic word: ').title()
#             if word ==  inp:
#                 result += 1
#             else:
#                 result -= 1
#         if result >= 1:
#             print(f'Voledemord magic words is {vold}')
#             return 'You win'
#         print(f'Voledemord magic words is {vold}')
#         return 'You lose'

# player = HarryPoter()
# print(player.win_voldemord())





