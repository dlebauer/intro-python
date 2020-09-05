# review last week
# operators
# logical
# variable names - no spaces!

# who did math homework?
# quiz: apples cost $1 and oranges cost $1.50
# create a variable for apples and one for oranges
# calculate the cost of 5 apples and 3 oranges
# how many oranges can you buy for $9? for $10?

## New
print("Hello world")

## String Substitution
# my name is Pat
myname = 'Pat'
greeting = 'Hello %s'
print(greeting % myname)

greeting = 'Hello %s'
names = ['Jens', 'Anya', 'Emil', 'Diza', 'Kalil']
print(greeting % names[1])

for x in names:
   print(x)
   

# for loops
for x in names:
   print(greeting % x)
   
for x in names:
  print(greeting % x)  

for x in (0,1):
  print(greeting % names[x])
   
# print sentence that says
# Happy _n_th birthday _name_
greeting = 'Hello %s, nice to meet you. you were born in %s'
names = ['David', 'Jens', 'Diza', 'Kalil', 'Anya', 'Emil']
years = [1975, 2010, 2007, 2008, 2011, 2008]



for i in (0,1,2,3,4,5): # or range(0,5)
  print(greeting % (names[i], years[i]))
