"""
1.  Delete all the assignments from last semester:
    https://classroom.github.com/classrooms/104235113-byui-cse-212-master

2.  Delete the template repositories (not the original prove-01, but the ones like
    byui-cse-212-master-f25-prove-01-prove-01-alt

    Use github cli gh to execute stuff like this:
    gh auth status
    gh auth refresh -h github.com -s delete_repo
    gh repo list -L 100 byui-cse-212 | awk '{print $1}'

    Then I drop that in Excel to run the delete repo commands like:
    (assuming it's in column A, I put this in B1:
    ="gh repo delete " & A1 & " --yes"
    which should expand to:
    gh repo delete byui-cse-212/byui-cse-212-master-w25-final-project-alt-final-project-alt --yes

3.  Recreate all the assignments from prove01-prove10, teach01-teach05, final-project in gh classroom
    - Note that prove-03 and teach-03 do not have a repository - skip those
    - Assignment names should be f25-prove-01 (for Fall 2025, prove 1 assignment)
    - Template repo should be byui-cse-212/prove-01-alt (until the alt gets removed)
    - take the link (https://classroom.github.com/a/knUcBiMV) and put it in the python code below

3.  Recreate all the assignments for the final-project in gh classroom
    - Note that prove-03 and teach-03 do not have a repository - skip those
    - Assignment names should be f25-prove-01 (for Fall 2025, prove 1 assignment)
    - Template repo should be byui-cse-212/prove-01-alt (until the alt gets removed)
    - take the link (https://classroom.github.com/a/knUcBiMV) and put it in the python code below

4.  Run this python script to update the links so that canvas points to this new semester's
    assignments (alts are for previous years)

5.  You are done, do NOT create a Roster in Github Classroom, the students can accept the assignments
    without the roster.
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
