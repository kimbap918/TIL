a, b = map(int, input().split()) 
c, d = map(int, input().split()) 
f = [] 
f.append(a / c + b / d) 
f.append(c / d + a / b) 
f.append(d / b + c / a) 
f.append(b / a + d / c) 
f_max = max(f) 
print(f.index(f_max))