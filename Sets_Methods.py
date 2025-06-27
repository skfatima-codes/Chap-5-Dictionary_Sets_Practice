s={4,5,6,78,8,"Fatima"}
print(s,type(s))
s.add(1)
s.copy()# ALways return a shallow copy of set
print(s)
#Difference It gives elements that are in set a but not in b.
a = {1, 2, 3}
b = {2, 3, 4}
print(a.difference(b))   # Output: {1}
#It checks if the two sets have no common elements.
# It returns True if they are completely different, else False
a1 = {1, 2}
b2 = {3, 4}
print(a.isdisjoint(b))   # Output: True


