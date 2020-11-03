players = 5
game = None
mySerial = 0

def serial2name(serial):
    global mySerial
    if serial == mySerial:
        return "you"
    else:
        return "Player %d" % serial