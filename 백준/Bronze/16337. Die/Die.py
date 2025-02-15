first = input()
second = input()
third = input()

if first == ":::" and second == ":o:" and third == ":::":
    print(1)
elif (first == "o::" and second == ":::" and third == "::o") or (first == "::o" and second == ":::" and third == "o::"):
    print(2)
elif (first == "o::" and second == ":o:" and third == "::o") or (first == "::o" and second == ":o:" and third == "o::"):
    print(3)
elif first == "o:o" and second == ":::" and third == "o:o":
    print(4)
elif first == "o:o" and second == ":o:" and third == "o:o":
    print(5)
elif (first == "ooo" and second == ":::" and third == "ooo") or (first == "o:o" and second == "o:o" and third == "o:o"):
    print(6)
else:
    print("unknown")