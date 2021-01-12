import execjs

with open('1.js', 'r') as f:
    js_code = f.read()

js_obj = execjs.compile(js_code)
sign=js_obj.eval("e('hello')")
print(sign)