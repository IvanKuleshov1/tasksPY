import re


def main(source):
    matches = re.findall("{\\s*equ\\s*(\\w*)\\s*<=(-?\\d*)}", source)
    response = {}
    for match in matches:
        response[match[1]] = int(match[2])
    return response


print(main("<block> equ arlaor <=-6582. </block>.<block> equ didibe_843 <=6157.</block>. <block> equ zaon<= 1840. "
           "</block>. <block>equ didi <= -1373.</block>."))
