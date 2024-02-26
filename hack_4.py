"""
generic script

text: "fooziman" output => "oozima" 
text: "barziman" output => "arzima" 
text: "qux" output => "qux" 
"""


def fn_hack_4(s):
    result = s
    no_mostrar = ["f", "b", "n"]
    _str = []

    for txt in result:
        if txt not in no_mostrar:
            _str.append(txt)
    result = "".join(_str)
    return result
a = fn_hack_4("fooziman")
b = fn_hack_4("barziman")
c = fn_hack_4("qux")
print(f"({a} {b} {c})")
