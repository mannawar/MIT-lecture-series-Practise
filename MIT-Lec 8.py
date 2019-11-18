# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 05:30:46 2019

@author: Mannawar Hussain
"""

#################
## EXAMPLE: simple Coordinate class
#################

class Coordinate (object):
     """A coordinate is made up of x and y values"""
     def __init__(self,x,y):
         """Set the x and y values"""
         self.x = x
         self.y = y
     def __str__(self):
        """Returns a strinf representation of self"""
        return "<" + str(self.x) + "," + str(self.y) + ">"
     def distance (self, other):
         """Returns the euclidean distance between two points"""
         x_diff_sq = (self.x - other.x)**2
         y_diff_sq = (self.y - other.y)**2
         return (x_diff_sq +y_diff_sq)**.5

c = Coordinate(3,4)
origin = Coordinate (0, 0)
print(c.x, origin.x)
print (c.distance(origin))
print(Coordinate.distance(c, origin))
print(origin.distance(c))
print(c)



#################
## EXAMPLE: simple class to represent fractions
## Try adding more built-in operations like multiply, divide
### Try adding a reduce method to reduce the fraction (use gcd)
#################

class Fraction (object):
    """"A number represented as a fraction"""
    
    def __init__(self, num, denom):
      """num and denom are integers"""
      assert type (num) == int and type (denom) == int, "ints not used"
      self.num = num
      self.denom = denom
    def __str__(self):
        """Return a string representation of self"""
        return str(self.num) + "/" + str(self.denom)
    def __add__(self, other):
        """Returns a new fraction representing addition"""
        top = self.num*other.denom + self.denom*other.num
        bott = self.denom*other.denom
        return Fraction(top, bott)
    def __sub__(self, other):
        """Returns a new fraction representing subtraction"""
        top = self.num*other.denom - self.denom*other.num
        bott = self.denom*other.denom
        return Fraction (top, bott)
    def __mul__(self, other):
        """Returns a new fraction representing multiplication of two fractions self and other"""
        top = self.num*other.num
        bott = self.denom*other.denom
        return Fraction(top, bott)
    def __float__(self):
        """ Returns a float value of a fraction"""
        return self.num/self.denom
    def inverse (self):
        """Returns 1/self value"""
        return Fraction (self.denom, self.num)
  
    
    
a = Fraction (1, 4)
b = Fraction (3, 4)
c= a + b         # c is a fraction object
d= a - b
e= a * b
print (d)
print (c)
print (e)
print (float(c))
print (Fraction.__float__(c))
print (float(b.inverse()))




##############
## EXAMPLE: a set of integers as class
##############

class intSet (object):
    """ An intset is a set of integers
    the value is represented by alist of ints, self.vals
    Each int in the set occurs in self.vals exactly once"""
    def __init__(self):
        """Creates an empty set of integers"""
        self.vals = []
    def insert(self, e):
        """Assume e is an integer and insert e into self"""
        if not e in self.vals:
            self.vals.append(e)
    def member(self, e):
        """Assume e is an integer
        Return True if e is in self, otherwise False"""
        return e in self.vals
    def remove (self, e):
        """ Assume e is an integer and remove e from self
        raise ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + 'not found')
    def __str__(self):
        "Returns a string representation of self"""
        self.vals.sort()
        return '{'+','.join([str(e) for e in self.vals]) +'}'
        
        
s = intSet()
print(s)
s.insert(3)
s.insert(4)
s.insert(3)
print (s)
s.member(3)
s.member(5)
s.insert(6)
print(s)
#s.remove(3)  # leads to an error
print(s)
s.remove(3)






































































































