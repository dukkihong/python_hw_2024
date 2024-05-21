class Point:

    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y

    def get(self):
        return (self.x,self.y)
    
class Rectangle:

    def __init__(self,x1,y1,x2,y2):
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2
        lt=Point(x1,y1)
        lt=Point.get(lt)
        rb=Point(x2,y2)
        rb=Point.get(rb)
        self.lt=lt
        self.rb=rb

    def show(self):
        print(f'좌측 상단 꼭지점이 ({self.lt})이고 우측 하단 꼭지점이 ({self.rb})인 사각형입니다.')

    def getWidth(self):
        res=self.x2-self.x1
        return res

    def getHeight(self):
        res=self.y2-self.y1
        return res
    
    def getArea(self):
        res=self.getWidth()*self.getHeight()
        return res

    def getPerimeter(self):
        res=2*(self.getWidth()+self.getHeight())
        return res

r1=Rectangle(5,5,20,10)
a=r1.getArea()
p=r1.getPerimeter()

r1.show()
print(f'넓이는 {a}, 둘레는 {p}')
