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
        return 'style'
    elif score == 2:
        return 'style'
    elif score == 3:
        return 'warning'
    elif score == 4:
        return 'warning'
    elif score == 5:
        return 'error'

def parse():
    # TODO: do this properly, using the xml module.
    # Write header
    sys.stderr.write('''<?xml version="1.0" encoding="UTF-8"?>\n''')
    sys.stderr.write('''<results version="2">\n''')
    sys.stderr.write('''  <cppcheck version=""/>\n''')
    sys.stderr.write('''  <errors>\n''')

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
        sys.stderr.write('''  <error id="%s" severity="%s" msg=%s>\n'''%(m['label'], severity, msg))
        sys.stderr.write('''    <location file="%s" line="%s"/>\n'''%(m['fname'], m['lineno']))
        sys.stderr.write('''  </error>\n''')

    # Write footer
    sys.stderr.write('''  </errors>\n''')
    sys.stderr.write('''</results>\n''')

if __name__ == '__main__':
    parse()
