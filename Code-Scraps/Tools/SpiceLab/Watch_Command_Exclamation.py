#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals, absolute_import, print_function, division

# sopel imports
import sopel.module


# imports for system and OS access, directories
import os
import sys

# imports based on THIS file
moduledir = os.path.dirname(__file__)
shareddir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(shareddir)
from BotShared import *

# Ensure Encoding
reload(sys)
sys.setdefaultencoding('utf-8')


"""
bot.nick do this
"""

# TODO make sure restart and update save database


@rule('(.*)')
@sopel.module.thread(True)
def bot_watch_exclamation_hub(bot, trigger):

    if not str(trigger).startswith(tuple(['!'])):
        return

    # don't run jobs if not ready
    while "botdict_loaded" not in bot.memory:
        pass

    bot_watch_exclamation(bot, trigger)
    botdict_save(bot)
