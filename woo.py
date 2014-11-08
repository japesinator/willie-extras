import willie

@willie.module.commands('woo')
def helloworld(bot, trigger):
    bot.say('WOOOOOOOOOOOOO!')
