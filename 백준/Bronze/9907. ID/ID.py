id_map = "JABCDEFGHIZ"
s = input()
id = int(s[0]) * 2 + int(s[1]) * 7 + int(s[2]) * 6 + int(s[3]) * 5 + int(s[4]) * 4 + int(s[5]) * 3 + int(s[6]) * 2
print(id_map[id % 11])
