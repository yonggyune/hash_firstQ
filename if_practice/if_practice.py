people =5 
apple = 20

if people < apple /5 :
    print ( "신나는 사과 파티 ! 배터지게 먹자!")

if apple%people >0 :
    print ("사과수가 맞지 않아 ! 몇 개는 쪼개 먹자! ")

if people > apple:
    print("사람이 너무 많아")

from datetime import datetime
hour = datetime.now().hour

if hour>12:
    print('오후입니다')

number = 15 

if number % 3 ==0:
    print (number,"는 3의 배수 입니다.",format(number))