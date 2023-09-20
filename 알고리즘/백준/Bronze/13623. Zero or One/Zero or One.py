lst_=list(map(int, input().split()))
 
if lst_[0]==lst_[1] and lst_[0]==lst_[-1]:
    print("*")
elif lst_[0]!=lst_[1] and lst_[0]!=lst_[-1] and lst_[1]==lst_[-1]:
    print("A")
elif lst_[1]!=lst_[0] and lst_[1]!=lst_[-1] and lst_[0]==lst_[-1]:
    print("B")
else:
    print("C")
