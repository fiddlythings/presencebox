# Presence Indicator LED Box POC
# Reagen B. Ward
# http://hackaday.io/project/1014-IM-Status-Indicator-Nameplates

# Sample launch script (baling wire) for the python / finch presence POC
#
# This script sets up dbus without needing an XServer running.  Screen is handy here, but not necessary.

dbus-launch screen -dmS "presencepoc"
screen -S "presencepoc" -p 0 -X stuff "finch$(printf \\r)"
screen -S "presencepoc" -X screen
screen -S "presencepoc" -p 1 -X stuff "python presencepoc.py$(printf \\r)"
