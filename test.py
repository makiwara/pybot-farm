from auth import create_bot
from javascript import require, On
mineflayer = require('mineflayer')
pathfinder = require('mineflayer-pathfinder')

bot = create_bot('TestBot')
RANGE_GOAL = 1

@On(bot, 'chat')
def handleMsg(self, sender, message, *args):
    if sender and (sender != self.username):
        bot.chat('Hi, you said ' + message)
        if 'come' in message:
            player = bot.players[sender]
            bot.chat("Coming!")
            target = player.entity
            if not target:
                bot.chat("I don't see you !")
                return
            pos = target.position
            bot.pathfinder.setGoal(pathfinder.goals.GoalNear(pos.x, pos.y, pos.z, RANGE_GOAL))

