  '''
  Given a string S as input which consists of multiple words separated by a space, the program must print
  the count C of the words which are repeated exactly N times. The comparison of the words is case
  sensitive.

  Example Input/Output 1:
  Input:
  one two three four three two five
  1
  Output:
  3
  Explanation:
  The words which are repeated only once are one, four and five. Hence the count is 3.
  Example Input/Output 2:
  Input:
  one two three four three two five one five Three
  2
  Output:
  4
  '''
  
st = input().split(" ")
k = int(input())
c=0
d ={}
for i in st:
    d[i]=0
for i in st:
    d[i]+=1
print(d)
for i in d:
    if(d[i]==k):
        c+=1
print(c)
