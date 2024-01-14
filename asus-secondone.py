def input_float():
    while(True):
        a_text = input("Input positive real number:")
        try:
            a = float(a_text)
            if(a <0):
                raise Exception
            return a
        except Exception:
            print("Your input wasn't positive real number")


print("This programm calculates square's aria")
a = input_float()
s = a * a
print("S = ", s)