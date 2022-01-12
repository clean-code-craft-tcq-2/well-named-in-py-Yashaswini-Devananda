majorColors = ['White', 'Red', 'Black', 'Yellow', 'Violet']
minorColors = ["Blue", "Orange", "Green", "Brown", "Slate"]

x = 1
print (f"{'Pair Number' : ^10} {'Major Color' : ^15} {'Minor Color' : ^15}");
for y in majorColors:
    for z in minorColors:
        print (f"{str(x) : ^10} {y : ^15} {z : ^15}");
        x+=1
