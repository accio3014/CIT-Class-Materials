# class_.py

class FourCal :

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def add(self) :     # class 내부에 있는 function을 method라고 부름, method를 만들때 무조건 self가 처음에 들어가야 함
        result = self.first + self.second

        return result
    
    def mul(self) :
        result = self.first * self.second

        return result
    
    def sub(self) :
        result = self.first - self.second

        return result
    
    def div(self) :
        result = self.first / self.second

        return result


# class 클래스(상속받을 클래스)
class MoreFourCal(FourCal) :    # FourCal 클래스를 상속 받았기 때문에 FourCal 클래스의 메서드를 사용할 수 있음
    def pow(self) :
        result = self.first ** self.second

        return result


class SafeFourCal(FourCal) :
    def div(self) :             # 상속을 받을때 기존 메소드의 내용을 변경할 수 있음, 이것을 method overriding 이라고 함
        if(self.second == 0) :
            return 0
        else :
            return self.first / self.second

a = FourCal(3, 7)       # a는 object, FourCal 클래스의 instance는 a
b = FourCal(10, 2)       # object 끼리는 서로 영향이 없음
print(a.first, a.second)
print(b.first, b.second)

print(a.add(), b.add())

c = MoreFourCal(5, 7)
print(c.add(), c.pow())

d = SafeFourCal(4, 0)
print(d.div())
