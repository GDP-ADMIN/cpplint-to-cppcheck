# CPPLint to CPPCheck
Script cpplint-to-cppcheckxml is used to convert cpplint xml result into cppcheck xml result. It is adapted from the same script [osrf/gazebo](https://bitbucket.org/osrf/gazebo/src/9b3dea9af2740ad0678f899c47b8aa17a953ceef/tools/cpplint_to_cppcheckxml.py?at=default) on bitbucket. This script uses [pygrok](https://github.com/garyelephant/pygrok) instead of regex. This script is created because the old implementation does not handle character [ in cpplint message segment.

# Installation
1. Install pygrok from https://github.com/garyelephant/pygrok
2. Copy file cpplint-to-cppcheckxml.py into /usr/local/bin
3. Make cpplint-to-cppcheck.py executable, `sudo chmod +x /usr/local/bin/cpplint-to-cppcheckxml.py`
