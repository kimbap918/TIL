passenger = 0
max_passenger = 0

for _ in range(10):
    out_train, in_train  = map(int, input().split()) 
    passenger += in_train - out_train 
    max_passenger = max(passenger, max_passenger) 
    
print(max_passenger)