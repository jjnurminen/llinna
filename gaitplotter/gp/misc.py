# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 15:31:11 2016

Misc functions for Gaitplotter (OS dialogs etc)

@author: Jussi
"""

import ctypes
import psutil
import sys


def nexus_pid():
    """ Tries to return the PID of the running Nexus process. """
    PROCNAME = "Nexus.exe"
    for proc in psutil.process_iter():
        try:
            if proc.name() == PROCNAME:
                return proc.pid
        except psutil.AccessDenied:
            pass
    return None

def error_exit(message):
    """ Custom error handler """
    # graphical error dialog - Windows specific
    ctypes.windll.user32.MessageBoxA(0, message, "Error in Nexus Python script", 0)
    sys.exit()

def messagebox(message):
    """ Custom notification handler """
    # graphical message dialog - Windows specific
    ctypes.windll.user32.MessageBoxA(0, message, "Message from Nexus Python script", 0)

def yesno_box(message):
    """ Yes/no dialog with message """
    return ctypes.windll.user32.MessageBoxA(0, message, "Question", 1) == 1
    
