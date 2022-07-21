test_score = int(input())
if test_score <= 100 and test_score >= 90:
    print("A") 
elif test_score <= 89 and test_score >= 80:
    print("B")
elif test_score <= 79 and test_score >= 70:
    print("C")
elif test_score <= 69 and test_score >= 60:
    print("D")
else:
    print("F")

