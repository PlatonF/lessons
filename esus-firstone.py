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

price = input_float("Input price for 1kg of candy: ")
for i in range(1, 11):
    price2 = round(price * i/10, 2)
    print("Price for {0}kg of candy is {1}".format(i/10, price2))