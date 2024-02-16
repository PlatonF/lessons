answer = None
for i in range(5):
    w = int(input(f"Input number № {i+1}:"))
    if(w % 5 == 0):
        answer = w
print(str(answer) + " is divisible by 5.")