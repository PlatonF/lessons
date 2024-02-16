answer = None
for i in range(5):
    w = float(input(f"Input number № {i+1}:"))
    if(answer == None):
        answer = w
    else:
        answer = max(w, answer)
print(str(answer) + " is biggest number.")