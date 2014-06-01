# !/usr/bin/env python

# Presence Indicator LED Box POC
# Reagen B. Ward
# http://hackaday.io/project/1014-IM-Status-Indicator-Nameplates
#
# Almost all credit goes to the FreeDesktop DBus tutorial which I 
# blatantly cribbed
# http://dbus.freedesktop.org/doc/dbus-python/doc/tutorial.html

# Check the HackADay link for info on what this does, but do know that 
# this code is from an early POC and is used with finch via DBus.

# You need to set up an user in OCS and add your office mates and yourself 
# as friends. Be sure to set aliases properly.  Replace NAME_ONE, NAME_TWO, 
# etc with legit names.
#
# Be sure to map gpio to LED properly.  I keep a copy of my map in comments 
# just to ensure it's handy.

# Yes, it's very ugly.  Yes, I could have saved a 500 lines of repetition.  
# This was for tinkering before I moved on to using libpurple itself.

import logging
import dbus
import gobject
import os
from dbus.mainloop.glib import DBusGMainLoop


dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
bus = dbus.SessionBus()
obj = bus.get_object("im.pidgin.purple.PurpleService", "/im/pidgin/purple/PurpleObject")
purple = dbus.Interface(obj, "im.pidgin.purple.PurpleInterface")

status_hash = {}


def update_status_hash(username, status):
    global status_hash
    if status_hash.has_key[username] and status_hash[username] == status:
        return False
    status_hash[username] = status
    return True


def buddy_status_changed(buddy, old_status, status):
    alias = purple.PurpleBuddyGetAlias(buddy)
    name = purple.PurpleBuddyGetName(buddy)
    status_id = purple.PurpleStatusGetId(status)
    status_text = purple.PurpleStatusGetAttrString(status, "message")
    print alias, name, status_id, status_text
    if alias == "NAME_ONE":
        if status_id == "available":
            os.system("/usr/local/bin/gpio -g write 24 0")
            os.system("/usr/local/bin/gpio -g write 25 1")
        elif status_id == "busy":
            os.system("/usr/local/bin/gpio -g write 24 1")
            os.system("/usr/local/bin/gpio -g write 25 0")
        elif status_id == "do-not-disturb":
            print "JIM DND"
            os.system("/usr/local/bin/gpio -g write 24 1")
            os.system("/usr/local/bin/gpio -g write 25 0")
        elif status_id == "away":
            os.system("/usr/local/bin/gpio -g write 24 1")
            os.system("/usr/local/bin/gpio -g write 25 1")
        else:
            os.system("/usr/local/bin/gpio -g write 24 1")
            os.system("/usr/local/bin/gpio -g write 25 1")

    elif alias == "NAME_TWO":
        if status_id == "available":
            os.system("/usr/local/bin/gpio -g write 18 0")
            os.system("/usr/local/bin/gpio -g write 23 1")
        elif status_id == "busy":
            os.system("/usr/local/bin/gpio -g write 18 1")
            os.system("/usr/local/bin/gpio -g write 23 0")
        elif status_id == "do-not-disturb":
            os.system("/usr/local/bin/gpio -g write 18 1")
            os.system("/usr/local/bin/gpio -g write 23 0")
        elif status_id == "away":
            os.system("/usr/local/bin/gpio -g write 18 1")
            os.system("/usr/local/bin/gpio -g write 23 1")
        else:
            os.system("/usr/local/bin/gpio -g write 18 1")
            os.system("/usr/local/bin/gpio -g write 23 1")
    elif alias == "NAME_THREE":
        if status_id == "available":
            os.system("/usr/local/bin/gpio -g write 4 1")
            os.system("/usr/local/bin/gpio -g write 22 0")
        elif status_id == "busy":
            os.system("/usr/local/bin/gpio -g write 22 1")
            os.system("/usr/local/bin/gpio -g write 4 0")
        elif status_id == "do-not-disturb":
            os.system("/usr/local/bin/gpio -g write 22 1")
            os.system("/usr/local/bin/gpio -g write 4 0")
        elif status_id == "away":
            os.system("/usr/local/bin/gpio -g write 22 1")
            os.system("/usr/local/bin/gpio -g write 4 1")
        else:
            os.system("/usr/local/bin/gpio -g write 22 1")
            os.system("/usr/local/bin/gpio -g write 4 1")
    elif alias == "NAME_FOUR":
        if status_id == "available":
            os.system("/usr/local/bin/gpio -g write 27 0")
            os.system("/usr/local/bin/gpio -g write 17 1")
        elif status_id == "busy":
            os.system("/usr/local/bin/gpio -g write 27 1")
            os.system("/usr/local/bin/gpio -g write 17 0")
        elif status_id == "do-not-disturb":
            os.system("/usr/local/bin/gpio -g write 27 1")
            os.system("/usr/local/bin/gpio -g write 17 0")
        elif status_id == "away":
            os.system("/usr/local/bin/gpio -g write 27 1")
            os.system("/usr/local/bin/gpio -g write 17 1")
        elif status_id == "offline":
            os.system("/usr/local/bin/gpio -g write 27 0")
            os.system("/usr/local/bin/gpio -g write 17 0")
        else:
            os.system("/usr/local/bin/gpio -g write 27 1")
            os.system("/usr/local/bin/gpio -g write 17 1")

    else:
        print "OTHER"
    if status_text and update_status_hash(alias, status_text):
        s = "%s\t%s" % (alias, status_text)


def show_all_status():
    for account in purple.PurpleAccountsGetAllActive():
        for buddy in purple.PurpleFindBuddies(account, ""):
            alias = purple.PurpleBuddyGetAlias(buddy)
            name = purple.PurpleBuddyGetName(buddy)
            presence = purple.PurpleBuddyGetPresence(buddy)
            status = purple.PurplePresenceGetActiveStatus(presence)
            status_id = purple.PurpleStatusGetId(status)
            status_text = purple.PurpleStatusGetAttrString(status, "message")
            if status_text and update_status_hash(alias, status_text):
                s = "%s - %s" % (alias, status_text)


bus.add_signal_receiver(buddy_status_changed,
                        dbus_interface="im.pidgin.purple.PurpleInterface",
                        signal_name="BuddyStatusChanged")

gobject.MainLoop().run()


# GPIO to LED Map
#
#1R 24
#1G 25
#2R 18
#2G 23
#3G 4
#3R 22
#4G 17
#4R 27
