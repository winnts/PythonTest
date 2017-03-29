def find_first_duplicate(str):
    str = str.replace(" ", "")
    for x in str:
        if str.lower().count(x.lower()) > 1:
            return x


new_str = 'fuck thisF shit'
print(find_first_duplicate(new_str))
