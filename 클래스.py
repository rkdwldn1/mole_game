class MyClass:
    def __init__(self, name):  # 이름
        self.name = name

    def set_age(self, age):  # 나이
        self.age = age

    def set_height(self, height):  # 키
        self.height = height

    def set_bloodType(self, bloodType):  # 혈액형
        self.bloodType = bloodType

    def set_MBTI(self, MBTI):  # mbti
        self.MBTI = MBTI

    def set_school(self, school):  # 학교
        self.school = school

    def set_Department(self, Department):  # 학과
        self.Department = Department

    def set_BirthDay(self, BirthDay):  # 생일
        self.BirthDay = BirthDay

    def set_constellation(self, constellation):  # 별자리
        self.constellation = constellation

    def set_home(self, home):  # 사는곳
        self.home = home

    def set_fvColor(self, fvColor):  # 좋아하는 색
        self.fvColor = fvColor

    def set_SisterNum(self, SisterNum):  # 자매 수
        self.SisterNum = SisterNum

    def set_fvFood(self, fvFood):  # 좋아하는 음식
        self.fvFood = fvFood

    def set_hobby(self, hobby):  # 취미
        self.hobby = hobby

    def set_phone(self, phone):  # 핸드폰
        self.phone = phone

    def set_fvSeason(self, fvSeason):  # 좋아하는 날씨
        self.fvSeason = fvSeason

    def set_fvCharacter(self, fvCharacter):  # 좋아하는 캐릭터
        self.fvCharacter = fvCharacter

    def set_fvWeather(self, fvWeather):  # 좋아하는 계절
        self.fvWeather = fvWeather

    def set_fvPerson(self, fvPerson):  # 좋아하는 사람
        self.fvPerson = fvPerson

    def set_Hairlen(self, Hairlen):  # 머리길이
        self.Hairlen = Hairlen


ac = MyClass("지우")
ac.set_age(20)
ac.set_height(160)
ac.set_bloodType("O형")
ac.set_MBTI("ISFJ")
ac.set_school("호서대학교")
ac.set_Department("정보통신")
ac.set_BirthDay("5월25일")
ac.set_constellation("쌍둥이자리")
ac.set_home("안성")
ac.set_fvColor("핑크")
ac.set_SisterNum("한명")
ac.set_fvFood("고기")
ac.set_hobby("산책")
ac.set_phone("아이폰 11")
ac.set_fvSeason("가을")
ac.set_fvCharacter("도라에몽")
ac.set_fvWeather("선선한날")
ac.set_fvPerson("아이유")
ac.set_Hairlen("long")

print(
    ac.name
    + "의 나이는 %d" % ac.age
    + " 키는 %d" % ac.height
    + " 혈액형은 %s" % ac.bloodType
    + " Mbti는 %s" % ac.MBTI
    + " 학교는 %s" % ac.school
    + " 학과는 %s" % ac.Department
    + " 생일은 %s" % ac.BirthDay
    + " 별자리는 %s" % ac.constellation
    + " 집은 %s" % ac.home
    + " 좋아하는 색은 %s " % ac.fvColor
    + " 형제관계는 %s" % ac.SisterNum
    + " 좋아하는 음식은 %s" % ac.fvFood
    + " 취미는 %s" % ac.hobby
    + " 핸드폰은 %s" % ac.phone
    + " 좋아하는 계절은 %s" % ac.fvSeason
    + " 좋아하는 캐릭터는 %s" % ac.fvCharacter
    + " 좋아하는 날씨는 %s" % ac.fvWeather
    + " 좋아하는 인물은 %s" % ac.fvPerson
    + " 머리길이는 %s" % ac.Hairlen
)
