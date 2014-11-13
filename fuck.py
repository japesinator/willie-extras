"""
fuck.py - Pretty obvious
Copyright 2014, Chris Higgins http://chigstuff.com
Licensed under the Eiffel Forum License 2.

http://willie.dfbta.net
"""
import willie
import random
@willie.module.commands('fuck')
def ball(bot, trigger):
    insults = ["I'm a fucking twat...", "I'm a useless piece of shit...", "I'm a backstabber, never trust me...", "I am a worthless machine..."]
    insult = random.randint(0, len(insults))
    bot.say(insults[insults]);

    
