"""
text: [{"a":"b"},{"c":"d"},{"e":"f"}] output => [{"1":"2"},{"3":"4"},{"5":"6"}]
"""


def fn_hack_10(s):
    result = []
    count = 1
    for item in s:
        ls= {}
        for key, _ in item.items():
            ls[str(count)] = str(count + 1)
            count += 2
        result.append(ls)
    return result

print(fn_hack_10([{"a": "b"}, {"c": "d"}, {"e": "f"}]))