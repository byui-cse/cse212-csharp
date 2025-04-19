links = [
    ("lesson01", "prove", "https://classroom.github.com/a/knUcBiMV", True, True),
    ("lesson02", "prove", "https://classroom.github.com/a/PM1Z35wZ", True, True),
    ("lesson04", "prove", "https://classroom.github.com/a/E0F1t5rw", True, True),
    ("lesson05", "prove", "https://classroom.github.com/a/9uGxuyU9", True, True),
    ("lesson06", "prove", "https://classroom.github.com/a/8PO0P2Hd", True, True),
    ("lesson07", "prove", "https://classroom.github.com/a/Om_1fTI0", True, True),
    ("lesson08", "prove", "https://classroom.github.com/a/Nc9BZ51D", True, True),
    ("lesson09", "prove", "https://classroom.github.com/a/-LqCaFGX", True, True),
    ("lesson01", "teach", "https://classroom.github.com/a/Ofd6qvle", True, True),
    ("lesson02", "teach", "https://classroom.github.com/a/QzdG83_Z", True, True),
    ("lesson04", "teach", "https://classroom.github.com/a/ocUUSKOR", True, True),
    ("lesson05", "teach", "https://classroom.github.com/a/nmTLs7G-", True, True),
    ("lesson10", "prove", "https://classroom.github.com/a/_xthzpbA", True, False),
]

for lesson, type, link, do_regular, do_alt in links:
    print(lesson)
    if do_regular:
        with open('docs/' + lesson + '/' + type + '-classroom.html', 'w') as file:
            file.write(f"""<!DOCTYPE html>
<meta charset="utf-8">
<title>Redirecting to {link}</title>
<meta http-equiv="refresh" content="0; URL={link}">
<link rel="canonical" href="{link}">""")
    if do_alt:
        with open('docs/' + lesson + '/' + type + '-classroom-alt.html', 'w') as file:
            file.write(f"""<!DOCTYPE html>
<meta charset="utf-8">
<title>Redirecting to {link}</title>
<meta http-equiv="refresh" content="0; URL={link}">
<link rel="canonical" href="{link}">""")
