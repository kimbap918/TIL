# NLCS: North London Collegiate School
# BHA: Branksome Hall Asia
# KIS: Korea International School
# SJA: St. Johnsbury Academy
school_list = ["North London Collegiate School", "Branksome Hall Asia", "Korea International School", "St. Johnsbury Academy"] 
word = input()
if word[0] == "N":
    print(school_list[0])
elif word[0] == "B":
    print(school_list[1])
elif word[0] == "K":
    print(school_list[2])
else:
    print(school_list[3])