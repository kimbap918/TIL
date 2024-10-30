while 1:
    s = input()
    if s == "EOI":
        break
    print("Found" if "nemo" in s.lower() else "Missing")
