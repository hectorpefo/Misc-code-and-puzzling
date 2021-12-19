
with open("test.txt", "w") as f:
	f.write("some content here\n")
	f.write("and more\n")

with open("test.txt", "r") as g:
	lines = g.read().splitlines()
	# see newline options for open
print(lines,len(lines))

print([x**2 + y for x in range(8) for y in (2,3) if x > 3])

print([z for z in zip([1,2,3],[8,9])])

print ((lambda x,y: x+2*y)(3,5))

print ([y for y in map(lambda x: x**2+1,(4,6,8))])

print ([y for y in filter(lambda x: x>4,range(9))])

print( any( x>4 for x in [1,2,3] ))

def bloo(w,y=3):
	print(w,y)
bloo(4)
bloo(4,9)

class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age
  def myfunc(abc):
    print("Hello my name is " + abc.name)
p1 = Person("John", 36)
p1.myfunc()
p1.doop = 9
print("The doop of p1 is",p1.doop)

#iterator function (enumerate also a built-in)
def enumerate(sequence, start=0):
    n = start
    for elem in sequence:
        yield n, elem
        n += 1

b = "frog"
print("hello {} doop {}{} hi".format('a',b,'c'))

#frozenset is a static set-like class

# is vs ==
a = [36]
b = [36]
print(a == b, a is b) # True, False

import re
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt) # True if match

try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")

import requests
stw_html = requests.get('http://mervsrunning.com').text

from bs4 import BeautifulSoup
soup = BeautifulSoup(stw_html,features="lxml")
print(soup.title, soup.p)


# In Sublime be sure to cntrl-shift P conda Activate Environment base.
# Also, conda settings needs to have run_through_shell be True.
# More plotting examples at 
# https://www.w3schools.com/python/matplotlib_intro.asp
import matplotlib.pyplot as plt
import matplotlib
plt.plot([1,10,2,3,7])
plt.show()