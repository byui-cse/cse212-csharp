"""
1.  Delete all the assignments from last semester:
    https://classroom.github.com/classrooms/104235113-byui-cse-212-master

2.  Delete the template repositories (not the original prove-01, but the ones like
    byui-cse-212-master-f25-prove-01-prove-01-alt

    Use github cli gh to execute stuff like this:
    gh auth status
    gh auth refresh -h github.com -s delete_repo
    gh repo list -L 100 byui-cse-212 | grep master | awk '{print $1}'

    Then I drop that in Excel to run the delete repo commands like:
    (assuming it's in column A, I put this in B1:
    ="gh repo delete " & A1 & " --yes"
    which should expand to:
    gh repo delete byui-cse-212/byui-cse-212-master-w25-final-project-alt-final-project-alt --yes

3.  Recreate all the assignments from prove01-prove10, teach01-teach05, final-project in gh classroom
    - Note that prove-03 and teach-03 do not have a repository - skip those
    - Assignment names should be f25-prove-01 (for Fall 2025, prove 1 assignment)
    - Template repo should be byui-cse-212/prove-01
    - take the link (https://classroom.github.com/a/knUcBiMV) and put it in the python code below

3.  Recreate all the assignments and the final-project in gh classroom
    - Note that prove-03 and teach-03 do not have a repository - skip those
    - Assignment names should be f25-prove-01 (for Fall 2025, prove 1 assignment)
    - Template repo should be byui-cse-212/prove-01
    - take the link (https://classroom.github.com/a/knUcBiMV) and put it in the python code below

4.  Run this python script to update the links so that canvas points to this new semester's
    assignments (alts are for previous years)

5.  You are done, do NOT create a Roster in Github Classroom, the students can accept the assignments
    without the roster.
"""

links = [
    ("lesson01", "prove", "https://classroom.github.com/a/ImjcAjh8", True, True),
    ("lesson02", "prove", "https://classroom.github.com/a/CjacNbNZ", True, True),
    ("lesson04", "prove", "https://classroom.github.com/a/9qRS5mSi", True, True),
    ("lesson05", "prove", "https://classroom.github.com/a/asMoextS", True, True),
    ("lesson06", "prove", "https://classroom.github.com/a/PDhSGue_", True, True),
    ("lesson07", "prove", "https://classroom.github.com/a/9fpUobY3", True, True),
    ("lesson08", "prove", "https://classroom.github.com/a/eTgEpZBc", True, True),
    ("lesson09", "prove", "https://classroom.github.com/a/T7Jm4i7j", True, True),
    ("lesson10", "prove", "https://classroom.github.com/a/9hz4sHYc", True, False),
    ("lesson11", "prove", "https://classroom.github.com/a/r3GD7TQX", True, False), # final project
    ("lesson01", "teach", "https://classroom.github.com/a/X2B_3Oc7", True, True),
    ("lesson02", "teach", "https://classroom.github.com/a/12qtq7Wc", True, True),
    ("lesson04", "teach", "https://classroom.github.com/a/w60mPv3_", True, True),
    ("lesson05", "teach", "https://classroom.github.com/a/I5sMr-5t", True, True),
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
