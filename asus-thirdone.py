def input_float(str):
    while(True):
        a_text = input(str)
        try:
            a = float(a_text)
            if(a < 0):
                raise Exception
            return a
        except Exception:
            print("Input must be positive real number")


print("This programm calculates rectangle's perimeter and aria")
a = input_float("Input a: ")
b = input_float("Input b: ")
p = (a + b) * 2
s = a * b
print("S = ", s)
print("P = ", p)