from initializations import ColorSets 

ColorSet = ColorSets()

MAJOR_COLORS = ColorSet.majorColors
MINOR_COLORS = ColorSet.minorColors

def reference_manual():
    pairNum = 1
    print (f"{'Pair Number' : ^10} {'Major Color' : ^15} {'Minor Color' : ^15}");
    for majorColor in MAJOR_COLORS:
        for minorColor in MINOR_COLORS:
            print (f"{str(pairNum) : ^10} {majorColor : ^15} {minorColor : ^15}");
            pairNum+=1
