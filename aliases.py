import sqlite3
from willie import module

def configure():
    conn = sqlite3.connect('aliases.db')
    cursor = conn.cursor()

    cursor.execute("create table if not exists aliases (keyword text, phrase text)")
    conn.commit()
    conn.close()

@module.commands('learn')
def learn(bot, trigger):
    configure()
    conn = sqlite3.connect('aliases.db')
    cursor = conn.cursor()

    result = trigger.group(2).split(' ',1)

    keyword = result[0]
    phrase = result[1]

    try:
        cursor.execute('insert into aliases values (?,?)', (keyword, phrase))
        conn.commit()
        conn.close()
    except:
        bot.say('Error: That keyword already exists. Do you want to update it?')

@module.commands('update')
def update(bot, trigger):
    configure()
    conn = sqlite3.connect('aliases.db')
    cursor = conn.cursor()

    result = trigger.group(2).split(' ',1)

    keyword = result[0]
    phrase = result[1]

    try:
        cursor.execute('update aliases set phrase=(?) where keyword=(?)', (phrase, keyword))
        conn.commit()
        conn.close()
    except:
        bot.say("Oops, an error occurred")

@module.commands('al')
def printAlias(bot, trigger):
    configure()
    conn = sqlite3.connect('aliases.db')
    cursor = conn.cursor()

    keyword = (trigger.group(2),)

    try:
        cursor.execute('select phrase from aliases where keyword=(?)', keyword)
	result = cursor.fetchone()
        bot.say(str(result[0]))
        conn.close()
    except:
        bot.say("That keyword doesn't exist")
