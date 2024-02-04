def input_float(str):
    while(True):
        a_text = input(str)
        try:
            a = float(a_text)
            if(a <= 0):
                raise Exception
            return a
        except Exception:
            print("Input must be positive real number")

a = 0
b = 0
success = False

while(not success):
    a = input_float("Input a: ")
    b = input_float("Input b, smaller then a: ") 
    if a <= b:
        print("b must be smaller than a")
    else:
        success = True

j = 0
while(a >= b):
    a-=b
    j+=1

print("b fits "+ str(j) +" full times in a")
