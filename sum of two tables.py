N=int(input("enter the length of the two list:  "))
TAB1=[]
TAB2=[]
for i in range (0,N):
    inte=int((input(f"enter a number for the case {i+1} for list 1:  ")))
    TAB1.append(inte)
for i in range (0,N):
    inte=int((input(f"enter a number for the case {i+1} for list 2:   ")))
    TAB2.append(inte)
TAB=[]

for i in range (0,N):
    int=TAB1[i]+TAB2[i]
    TAB.append(int)
print(TAB)