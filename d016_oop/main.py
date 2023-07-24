# # import another_module
# # print(another_module.another_valuable)
#
# # import turtle
# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("DeepPink2")
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

# TODO 1: prettyt~ 패키지에서 PrettyT~ '클래스'(객체를 생성하기 위한 청사진)를 불러옴
from prettytable import PrettyTable
table = PrettyTable() # 실제로 객체가 완성되려면 ()를 붙여줌 -> table변수에 PrettyT~ 객체가 포함되었다

# TODO 1-a: 객체에 접근한 후 '메소드' 호출
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"]) # table변수에 add~()메소드(m아이콘)를 호출
table.add_column("Type", ["Electric", "Water", "Fire"])

# TODO 1-b: 객체에 접근한 후 속성을 변경
table.align = 'l' # 점연산자 찍으면 목록이 뜨는데 거기서 f아이콘 붙은 것들
print(table.align)
## {'base_align_value': 'c', 'Pokemon Name': 'l', 'Type': 'l'}

print(table)