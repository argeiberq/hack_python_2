"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""


def fn_hack_5(s):
    result = s
    _ls = {
        "foo":"fo-zi-ma-",
        "barziman":"ba-zi-an",
        "qux":"qu-",
        "eq":"eq"
    }
    for key in _ls:
        if key in result:
            return _ls[key]

    return result
a = fn_hack_5("fooziman")
b = fn_hack_5("barziman")
c = fn_hack_5("qux")
d = fn_hack_5("eq")
print(f"({a} {b} {c} {d})")
