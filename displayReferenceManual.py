from initializations import ColorSets 

ColorSet = ColorSets()

MAJOR_COLORS = ColorSet.majorColors
MINOR_COLORS = ColorSet.minorColors

x = 1
print (f"{'Pair Number' : ^10} {'Major Color' : ^15} {'Minor Color' : ^15}");
for y in MAJOR_COLORS:
    for z in MINOR_COLORS:
        print (f"{str(x) : ^10} {y : ^15} {z : ^15}");
        x+=1
