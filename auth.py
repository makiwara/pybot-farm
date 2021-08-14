'''
# Create '_credentials.py' and put this in:
HOST = '<host or ip>'
PORT = 25588
'''
from _credentials import HOST, PORT

from javascript import require, On
mineflayer = require('mineflayer')
pathfinder = require('mineflayer-pathfinder')


def create_bot(username, on_spawn = None) :
    bot = mineflayer.createBot({
        'host': HOST,
        'port': PORT,
        'username': username
    })
    bot.loadPlugin(pathfinder.pathfinder)

    @On(bot, 'error')
    def error(*args):
	    print("Error!", args)
    
    @On(bot, "end")
    def end(*args):
        print("Bot ended!", args)

    @On(bot, 'spawn')
    def handle(*args):
        print("I spawned 👋")
        mcData = require('minecraft-data')(bot.version)
        movements = pathfinder.Movements(bot, mcData)
        bot.pathfinder.setMovements(movements)
        if on_spawn is not None:
            on_spawn(*args)

    return bot


