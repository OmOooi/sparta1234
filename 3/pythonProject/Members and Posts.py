# ----- 코드 정의 ------
import hashlib

class Member:
    def __init__(self, name, username, password):
        self.name=name
        self.username=username
        self.password=password

    def display(self):
        print(self.name)
        print(self.username)

class Post:
    def __init__(self, title, content, auther):
        self.title=title
        self.content=content
        self.auther=auther


m1 = Member(name="ssindi", username="cindi", password="124578")
m2 = Member(name="ssindi2", username="cindi2", password="124578")
m3 = Member(name="ssindi3", username="cindi3", password="124578")
p1 = Post(title="cinditi1", content="cindico1", auther=m1.username)
p2 = Post(title="cinditi2", content="cindico2", auther=m1.username)
p3 = Post(title="cinditi3", content="cindico3", auther=m1.username)
p4 = Post(title="cinditi4", content="cindico4", auther=m2.username)
p5 = Post(title="cinditi5", content="cindico5", auther=m2.username)
p6 = Post(title="cinditi6", content="cindico6", auther=m2.username)
p7 = Post(title="cinditi7", content="cindico7", auther=m3.username)
p8 = Post(title="cinditi8", content="cindico8", auther=m3.username)
p9 = Post(title="cinditi9", content="cindico9", auther=m3.username)

# ----- 코드 실행 ------
Member.display(m1)
Member.display(m2)
Member.display(m3)

members = []
members.append(m1)
members.append(m2)
members.append(m3)

for i in members:
  #  Member.display(i)
    print(i.name)

posts = []
posts.append(p1)
posts.append(p2)
posts.append(p3)
posts.append(p4)
posts.append(p5)
posts.append(p6)
posts.append(p7)
posts.append(p8)
posts.append(p9)

for p in posts:
    if p.auther == "cindi":
        print(p.title)

for o in posts:
    if o.content == "cindico5":
        print(o.title)

for B in members:
    string = B.password
    hash_object = hashlib.sha256(string.encode())
    hex_dig = hash_object.hexdigest()
    print(hex_dig)



while True:
    user_input = input("생성할 Member 인스턴스와 Post 인스턴스를 고르세요 (M/P), 또는 검산을 고르세요.(K)")
    if user_input == "M" or user_input == "m":

        user_name_input = input("name을 입력하세요")
        user_username_input = input("username을 입력하세요")
        user_password_input = input("password를 입력하세요")

        m = Member(name=user_name_input, username=user_username_input, password=user_password_input)
        members.append(m)
        print("검산을 시도합니다(인스턴스의 존재를 확인합니다)")
        for T in members:
            print(T.name)
            print(T.username)
            print(T.password)
        print('완료되었습니다')

    if user_input == "P" or user_input == "p":

        user_title_input = input("title을 입력하세요")
        user_content_input = input("content를 입력하세요")
        user_auther_input = input("auther을 입력하세요")
        p = Post(title=user_title_input, content=user_content_input, auther=user_auther_input)
        posts.append(p)
        print("검산을 시도합니다(인스턴스의 존재를 확인합니다)")
        for j in posts:
            print(j.title)
            print(j.content)
            print(j.auther)
        print('완료되었습니다')

    if user_input == "K" or user_input == "k":
        user_k_input = input("검산할 대상을 선택하시오 members or posts (M/P)")
        if user_k_input == "M" or user_k_input == "m":
            for G in members:
                print(G.name)
                print(G.username)
                print(G.password)
            print('완료되었습니다')
        if user_k_input == "P" or user_k_input == "p":
            for L in posts:
                print(L.title)
                print(L.content)
                print(L.auther)
            print('완료되었습니다')
