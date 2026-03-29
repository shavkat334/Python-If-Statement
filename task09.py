a, b, c = int(input()), int(input()), int(input())
if a == b == c: print("Teng tomonli")
elif a == b or b == c or a == c: print("Teng yonli")
else: print("Turli tomonli")