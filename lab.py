class car:               # 클래스
    def drive(self):     # 메소드
        self.speed = 10  # 속성

mycar = car()                 #클래스로부터 객체의 생성
mycar.color = "blue"        #객체에 속성을 추가
mycar.model="Hyundai"   #객체에 속성을 추가
mycar.drive()                  #객체안의 메소드를 호출
print(mycar.speed)           #객체안의 속성을 참조
print(mycar.model)