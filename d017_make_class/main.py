class User:
    pass


user_1 = User()     # 객체 만들기

# 클래스에 속성 부여하긩! - 속성은 객체와 관련된 변수당
user_1.id = "001"
user_1.username = "no jam"

print(user_1.username)

# 다른 객체에 같은 속성 부여해주려면 이케이케 번거롭게 다 해줘야 햄?
user_2 = User()
user_2.id = "002"
user_2.usrname = "urrrrrgh"     # 이케 오타날 수도 이짜나

# 그래서 생성자라는 걸 이용한대
# 다르게 말하면 객체를 초기화하는 거라는디?


class Constructor:

    def __init__(self):     # 새로운 객체가 생성될 때마다 이게 실행될 거래
        print("new user being created...")


# 이케 말여
constructor_1 = Constructor()
constructor_1.id = "001"
constructor_1.username = "gwang gwang"

print(constructor_1.username)

constructor_2 = Constructor()
constructor_2.id = "002"
constructor_2.usrname = "oeoeeoji"


class Attribute:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.follower = 0       # 이케 기본값 정해주는 건 __init__()에 매개변수 필요음슴


my_attr = Attribute("001", "Aha")

my_attr.id = "001"      # 이렇게 하는 게 위에 def하고 객체 만든 거랑 똑같은 거란 뜻임
my_attr.username = "Aha"        # 근데 위에 있는 방법으로 하면 같은 속성 계속 부여해야 할 때 편하다고 ㅇㅇ


# 이제 메소드를 추가해볼 건데 함수 정의하는 거랑 똑같음
class Car:

    def __init__(self, seats):
        self.seats = seats

    def enter_race_mode(self):
        self.seats = 2


my_car = Car(5)
my_car.enter_race_mode()        # 이케 하는 거임


# 와 근데 이거는 좀 헷갈린다 ㅠㅠ 인스타 같은 거 만든다 쳐
class Insta:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):     # 객체가 user를 follow(user)하면
        user.followers += 1     # 이 객체랑 아마도 같은 형태의 객체일 user의 followers 속성이 1 증가하고
        self.following += 1     # 이 객체는 following 속성이 1 증가하게 만든 거


insta_1 = Insta("001", "Shinhwa")
insta_2 = Insta("002", "Nuest")

insta_1.follow(insta_2)     # insta_1이 insta_2를 follow한 거임

print(insta_1.followers)
print(insta_1.following)
print(insta_2.followers)
print(insta_2.following)


# 와 뭔데 알고 나니까 또 재미있고 난리
# 아니 그니까 알려주고 해야지 무작정 하라 그러면 어쩌란 거임 ㅠㅠㅠㅠㅠ 16일차는 너무 했음
