def rgb(r, g, b):
    round = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(round(r), round(g), round(b))

print(rgb(0, 2, 3))
print(rgb(255, 255, 255))