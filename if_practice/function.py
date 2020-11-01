def print_sqrt():
    r1 = (-b+(b**2-4*a*c)**0.5)/(2*a)
    r2 = (-b-(b**2-4*a*c)**0.5)/(2*a)

    print ('해는 {} 또는 {}'.format(r1,r2))


a=1
b=2
c=-8

#근의 공식은 a*x^2 +b*x+c =0 , a!=0 인 x에 관한 2차 방적식에 대해

print_sqrt()


def pyeongun():
    result=(enlish+math+korean+science)/4
    return(result)


enlish = 80
print('영어점수 =',enlish)
print()
math = 90
print('수학점수 =',math)
print()
korean = 70
print('국어점수 =',korean)
print()
science = 85
print('과학점수 =',science)
print()

print('평균 =',pyeongun())

print('어때요 참 쉽죠?')

### 매개 변수 ###

def print_sqrt(a,b,c):
    r1 = (-b+(b**2-4*a*c)**0.5)/(2*a)
    r2 = (-b-(b**2-4*a*c)**0.5)/(2*a)

    print ('해는 {} 또는 {}'.format(r1,r2))

x=2
y=-6
z=-8
print_sqrt(x,y,z)


def add_10(value):
    #value에 10을 더한 값을 올려주는 함수
    result = value+10
    return result


n = add_10(42)
print(n)