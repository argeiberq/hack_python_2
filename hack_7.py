"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [] output => [0] 
"""


def fn_hack_7(input_list):
    list_salida = []
    for item, _ in enumerate(input_list, 1):
        if item % 2 == 1:
            list_salida.append(str(item))
        else:
            list_salida.append(int(item))
    if not input_list:
        list_salida.append(int("0"))
    return list_salida
a = fn_hack_7(["a", "b", "c", "d", "e"])
b = fn_hack_7([])
print(f"{a}{b}")