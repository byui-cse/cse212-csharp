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
    ("lesson01", "prove", "https://classroom.github.com/a/zew8343a", True, True),
    ("lesson02", "prove", "https://classroom.github.com/a/bcMFBKVd", True, True),
    ("lesson04", "prove", "https://classroom.github.com/a/5ddCZjKA", True, True),
    ("lesson05", "prove", "https://classroom.github.com/a/x_LM7D3V", True, True),
    ("lesson06", "prove", "https://classroom.github.com/a/CNvHho1I", True, True),
    ("lesson07", "prove", "https://classroom.github.com/a/7-wdhRSR", True, True),
    ("lesson08", "prove", "https://classroom.github.com/a/-bHgia0S", True, True),
    ("lesson09", "prove", "https://classroom.github.com/a/-9nfB1Xm", True, True),
    ("lesson10", "prove", "https://classroom.github.com/a/igg5eSYR", True, False),
    ("lesson01", "teach", "https://classroom.github.com/a/pnO22Paq", True, True),
    ("lesson02", "teach", "https://classroom.github.com/a/PERK7G0g", True, True),
    ("lesson04", "teach", "https://classroom.github.com/a/XALMmsxW", True, True),
    ("lesson05", "teach", "https://classroom.github.com/a/L7HIj3-5", True, True),
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
