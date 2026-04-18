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
    # final project
    ("lesson11", "prove", "https://classroom.github.com/a/_sMIC4-b"),
    # prove 1-2,4-10
    ("lesson01", "prove", "https://classroom.github.com/a/CDrIO3Dc"),
    ("lesson02", "prove", "https://classroom.github.com/a/-p8HD-fF"),
    ("lesson04", "prove", "https://classroom.github.com/a/l7nMuM9c"),
    ("lesson05", "prove", "https://classroom.github.com/a/JtMCcnVA"),
    ("lesson06", "prove", "https://classroom.github.com/a/sxL_fDhD"),
    ("lesson07", "prove", "https://classroom.github.com/a/Rl-hFSpU"),
    ("lesson08", "prove", "https://classroom.github.com/a/9V9E1qUi"),
    ("lesson09", "prove", "https://classroom.github.com/a/lKpbkxHk"),
    ("lesson10", "prove", "https://classroom.github.com/a/bjK0tZY9"),
    # teach 1-2, 4-5
    ("lesson01", "teach", "https://classroom.github.com/a/k2cyZ0OH"),
    ("lesson02", "teach", "https://classroom.github.com/a/7KZU6gQY"),
    ("lesson04", "teach", "https://classroom.github.com/a/NjQIIM9R"),
    ("lesson05", "teach", "https://classroom.github.com/a/AFP9u45h"),
]

for lesson, type, link in links:
    print(lesson)
    with open('docs/' + lesson + '/' + type + '-classroom.html', 'w') as file:
        file.write(f"""<!DOCTYPE html>
<meta charset="utf-8">
<title>Redirecting to {link}</title>
<meta http-equiv="refresh" content="0; URL={link}">
<link rel="canonical" href="{link}">""")
