# Comments begin with a '#' and end at the end of the line

# Exercise 1
def ex1(str):
  d = {}
  for i in str:
    if i in d:
      d[i] += 1
    else:
      d[i] = 1

  for i in d:
    if d[i] > 1:
      print(i)

print("Ex1:")
ex1("hello world")

#Exercise 2
def ex2(str):
  d = {}
  for i in str:
    if i in d:
      d[i] += 1
    else:
      d[i] = 1

  for i in d:
      print(i, d[i])

print("Ex2: ")
ex2("hello world")

#Exercise 3
def ex3(l):
  list_set = set(l)
  print(list_set)


print("Ex3: ")
ex3([1,2,3,3,3,1,2,4,5,6])