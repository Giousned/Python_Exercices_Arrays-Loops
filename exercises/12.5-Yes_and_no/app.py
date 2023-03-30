theBools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

#Your code go here:

def asign_new_value(boleano):
    if boleano == 1:
        return "wiki"
    else:
        return "woko"

new_list = list(map(asign_new_value, theBools))

print(new_list)


