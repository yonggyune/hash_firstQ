scissor = '가위'
rock = '바위'
paper = '보'

win = '이겼다'
draw = '비겼다'
lose = '졌다'

mine = scissor
yours = rock

if mine == yours:
    result = draw

elif mine == scissor :
    if yours == rock:
        result = lose
    else:
        result = win

elif mine == rock:
    if yours == paper:
        result = lose
    else :
        result = win
else:
    if yours == rock:
        result = lost
    else :
        result = win


print(result)