import sys

# The following two functions check if the input values are genuinely hex or rgb
def is_hex_code(number):
    try:
        int(number,16) + 5
        return True
    except:
        return False
def is_rgb(r,g,b):
    try:
        int(r) + int(g) + int(b)
        return True
    except:
        return False

# This part uses those two functions to fully check the inputs
try:
    hex_code = False
    rgb = False
    if len(sys.argv) == 2:
        if is_hex_code(sys.argv[1]) and len(sys.argv[1]) == 6:
            hex_code = True
        else:
            raise ValueError()
    elif len(sys.argv) == 4:
        if is_rgb(sys.argv[1],sys.argv[2],sys.argv[3]):
            rgb = True
        else:
            raise ValueError()
    else:
        raise ValueError()

except:
    print("Usage: python3 hexcode_to_rgb.py <hexcode>")
    print("OR")
    print("python3 hexcode_to_rgb.py <r> <g> <b>")
    rgb = False
    hex_code = False
    

def hex_to_rgb():
    result = dict()
    result["red"],result["green"],result["blue"] = sys.argv[1][:2], sys.argv[1][2:4], sys.argv[1][4:]
    red,green,blue = int(result["red"],16),int(result["green"],16),int(result["blue"],16)
    return f"({red},{green},{blue})"
def rgb_to_hex():
    my_list = hex(int(sys.argv[1]))[2:],hex(int(sys.argv[2]))[2:],hex(int(sys.argv[3]))[2:]
    result = ""
    for hexa in my_list:
        if len(hexa) == 2:
            result += hexa.upper()
        else:
            result += f"0{hexa}"
    return result

if hex_code:
    print(hex_to_rgb())
elif rgb:
    print(rgb_to_hex())

     
