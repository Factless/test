class Dot:
    def __init__(self, x, y):
     self.x = x
     self.y = y
  #  def __eq__(self, other):
a = Dot(1 , 1)
b = Dot(3 , 2)
c = Dot(1 , 1)

print(a == c)