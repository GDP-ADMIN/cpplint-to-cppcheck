#!/usr/bin/env python

# Convert output from Google's cpplint.py to the cppcheck XML format for
# consumption by the Jenkins cppcheck plugin.

# Reads from stdin and writes to stderr (to mimic cppcheck)


import sys
import pygrok
import xml.sax.saxutils

def cpplint_score_to_cppcheck_severity(score):
    # I'm making this up
    if score == 1:
        return 'cpplint style'
    elif score == 2:
        return 'cpplint style'
    elif score == 3:
        return 'cpplint warning'
    elif score == 4:
        return 'cpplint warning'
    elif score == 5:
        return 'cpplint error'

def parse():
    # TODO: do this properly, using the xml module.
    # Write header
    sys.stderr.write('''<?xml version="1.0" encoding="UTF-8"?>\n''')
    sys.stderr.write('''<results>\n''')

    pattern="%{DATA:fname}:%{INT:lineno}: %{GREEDYDATA:rawmsg} \[%{DATA:label}\] \[%{INT:severity}"

    for l in sys.stdin.readlines():
        m = pygrok.grok_match(l.strip(), pattern)
        if not m:
            continue
        if len(m.keys()) != 5:
            continue
        # Protect Jenkins from bad XML, which makes it barf
        msg = xml.sax.saxutils.quoteattr(m['rawmsg'])
        severity = cpplint_score_to_cppcheck_severity(int(m['severity']))
        sys.stderr.write('''<error file="%s" line="%s" id="%s" severity="%s" msg=%s/>\n'''%(m['fname'], m['lineno'], m['label'], severity, msg))

    # Write footer
    sys.stderr.write('''</results>\n''')

if __name__ == '__main__':
    parse()
