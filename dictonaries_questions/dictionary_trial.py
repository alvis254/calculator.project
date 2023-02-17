dic = {}
while True:
    product = input("enter the product name(enter q for quit)=")
    if product == "q" or product == "Q":
        break
    else:
        price = input("enter the price of the product=")
        dic[product] = price

while True:
    name = input("enter the name of the product that you entered(enter q for quit)=")  
    if name == "q" or name == "Q":
        break
    else:
        if name is not dic:
            print("name of the product is invalid")

        print("price of the product=",dic[name])
                    