"""
1. delete all the assignments from last semester
2. remove the student roster

Use github cli gh to execute stuff like this:
gh auth status
gh repo list -L 100 byui-cse212 | awk '{print $1}'
Then I drop that in excel to run the delete repo commands like:
gh repo delete byui-cse212/byui-cse212-classroom-w25-final-project-alt-final-project-alt --yes

recreate all the assignments from prove01-prove10, teach01-teach05, final-project in gh classroom

using excel I did something like this per row:
1	byui-cse212/prove-01-alt	s25-prove-01		lesson01	prove	https://classroom.github.com/a/knUcBiMV
to generate the links array down below

run this python script to update the links files (alts are for previous years)

add the student roster back in (student-000, student-001, ..., student-300)
"""

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
