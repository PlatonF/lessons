answer = None
for i in range(5):
    w = int(input(f"Input number № {i+1}:"))
    if(w % 6 == 0):
        if(answer == None):
            answer = w
        else:
            answer = max(w, answer)
print(str(answer) + " is biggest number divisible by 6.")