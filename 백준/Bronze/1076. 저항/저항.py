import sys

resistance = {"black":[0,1], "brown":[1,10],
              "red":[2,100],"orange":[3,1000],
              "yellow":[4,10000],"green":[5,100000],
              "blue":[6,1000000],"violet":[7,10000000],
              "grey":[8,100000000],"white":[9,1000000000]}
result = ''

color1 = sys.stdin.readline().rstrip()
color2 = sys.stdin.readline().rstrip()
color3 = sys.stdin.readline().rstrip()

result = int(str(resistance[color1][0]) + str(resistance[color2][0]))*resistance[color3][1]
print(int(result)) 