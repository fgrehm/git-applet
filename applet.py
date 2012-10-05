#!/usr/bin/env python
import sys
import gtk
import appindicator

import os

PING_FREQUENCY=5
DIR=os.getcwd()

class GitApplet:
    def __init__(self):
        self.ind = appindicator.Indicator("new-gmail-indicator",
                                           DIR + '/git_icon.png',
                                           appindicator.CATEGORY_APPLICATION_STATUS)
        self.ind.set_status(appindicator.STATUS_ACTIVE)
        self.ind.set_attention_icon("new-messages-red")

        self.menu_setup()
        self.ind.set_menu(self.menu)

    def menu_setup(self):
        self.menu = gtk.Menu()

        self.quit_item = gtk.MenuItem("Quit")
        self.quit_item.connect("activate", self.quit)
        self.quit_item.show()
        self.menu.append(self.quit_item)

    def main(self):
        # self.check_repositories()
        gtk.timeout_add(PING_FREQUENCY * 1000, self.check_repositories)
        gtk.main()

    def quit(self, widget):
        sys.exit(0)

    def check_repositories(self):
        # The magic happens here
        self.ind.set_icon(DIR + '/git_icon_red.png')
        print("should have changed icon")
        # os.system('notify-send "Checking..."')
        return True

if __name__ == "__main__":
    indicator = GitApplet()
    indicator.main()
