s = "hello"

try:
    s[0] = "H"
except TypeError as e:
    print("Error:", e)
