class RegularPolygon:
  
  def __init__(self,L,N):
    self.L = L
    self.N = N

  def side(self):
    return self.L
    
  def perimeter(self):
    return self.L * self.N

test = RegularPolygon(5,3)

print "Perimeter:", test.perimeter()
print "Side:", test.side()