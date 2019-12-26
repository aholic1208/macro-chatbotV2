#Importing discord.py and shit
import discord
import asyncio

#This is a 1.4.7 chatbot. Not based on anything. WooLoo 1, Cubert 1

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in. wooloo 1, cubert 1') #Prints out a nice message to wooloo and cubert :)
    oldline = 'Innitial message.'
    while True: #Main loop
        logFile = open("wooloogets1.nd") #Loads the log file.
        with logFile as f:
            lines = f.read().splitlines()
            await asyncio.sleep(0.2) #We need to stop it for a bit before reading last line beacuse python gay.
            last_line = lines[-1] #Read last line.
            last_line = last_line.replace('@',"I am a stupid faggot that just tried to ping someone. ") #Removes niggas tryna ping other niggas.
            last_line = last_line.replace('Chat',"") #Remove the ugly 'Chat' before every message
            if oldline != last_line: #Check if the oldline is different from the last line.
                oldline = last_line #Sets the oldline as the last line in the log file.
                print('Ready to send message:' + last_line) #Prints what message its about to send.
                chatbotChannel = client.get_channel(UR CHANNEL HERE) #Sets the channel that the message is gonna get sent in.
                await chatbotChannel.send(last_line) #Sends the message.

client.run('Private bot key here.') #Runs the bot.
