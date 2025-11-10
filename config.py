'''
Manage config
'''

from aqt import mw

CONFIG = mw.addonManager.getConfig(__name__)

def save_config():
    mw.addonManager.writeConfig(__name__, CONFIG)
