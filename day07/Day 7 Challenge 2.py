wireMap = {"b": 16076}

def isinteger(signal_value):
    try:
        int(signal_value)
        return True
    except ValueError:
        return False


def dealwithnotgate(signal_value, into_wire):
    notwire = str(signal_value).replace("NOT ", "")
    if notwire in wireMap:
        wireMap[into_wire] = ~ wireMap[notwire]


def dealwithandgate(signal_value, into_wire):
    two_values = str(signal_value).split(" AND ")
    if two_values[0] in wireMap and two_values[1] in wireMap:
        wireMap[into_wire] = wireMap[two_values[0]] & wireMap[two_values[1]]
    elif isinteger(two_values[0]) and two_values[1] in wireMap:
        wireMap[into_wire] = int(two_values[0]) & wireMap[two_values[1]]
    elif two_values[0] in wireMap and isinteger(two_values[1]):
        wireMap[into_wire] = wireMap[two_values[0]] & int(two_values[1])
    elif isinteger(two_values[0]) and isinteger(two_values[1]):
        wireMap[into_wire] = int(two_values[0]) & int(two_values[1])


def dealwithorgate(signal_value, into_wire):
    two_values = str(signal_value).split(" OR ")
    if two_values[0] in wireMap and two_values[1] in wireMap:
        wireMap[into_wire] = wireMap[two_values[0]] | wireMap[two_values[1]]
    elif isinteger(two_values[0]) and two_values[1] in wireMap:
        wireMap[into_wire] = int(two_values[0]) | wireMap[two_values[1]]
    elif two_values[0] in wireMap and isinteger(two_values[1]):
        wireMap[into_wire] = wireMap[two_values[0]] | int(two_values[1])
    elif isinteger(two_values[0]) and isinteger(two_values[1]):
        wireMap[into_wire] = int(two_values[0]) | int(two_values[1])


def dealwithlshiftgate(signal_value, into_wire):
    shift_parts = str(signal_value).split(" LSHIFT ")
    if shift_parts[0] in wireMap:
        wireMap[into_wire] = int(wireMap[shift_parts[0]]) << int(shift_parts[1])


def dealwithrshiftgate(signal_value, into_wire):
    shift_parts = str(signal_value).split(" RSHIFT ")
    if shift_parts[0] in wireMap:
        wireMap[into_wire] = int(wireMap[shift_parts[0]]) >> int(shift_parts[1])


while "a" not in wireMap:
    counter = 0
    with open("input.txt") as inputFile:
        for line in inputFile:
            parts = line.replace("\n", "").split(" -> ")
            signal = parts[0]
            wire = parts[1]

            if wire == "b":
                continue  # don't override the value

            if signal.__contains__("NOT"):
                dealwithnotgate(signal, wire)
            elif signal.__contains__("AND"):
                dealwithandgate(signal, wire)
            elif signal.__contains__("OR"):
                dealwithorgate(signal, wire)
            elif signal.__contains__("LSHIFT"):
                dealwithlshiftgate(signal, wire)
            elif signal.__contains__("RSHIFT"):
                dealwithrshiftgate(signal, wire)
            else:  # just an assignment
                if isinteger(signal):
                    wireMap[wire] = int(signal)
                else:  # must be a letter assigning from somewhere else
                    if signal in wireMap:
                        wireMap[wire] = wireMap[signal]  # copy existing signal into wire
                    else:
                        print "Value doesn't exist yet for ", signal
    print wireMap
print "Value of a is",  wireMap["a"]
