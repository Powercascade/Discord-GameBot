import discord
from discord.ext import commands
from config import *
from tictactoe import *
from imageFile import *
import random

# makes a bot called "bot" with the "!" prefix
bot = commands.Bot(command_prefix=PREFIX, description="!help for list of commands")
bot.remove_command('help')

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} and connected to Discord! (ID: {bot.user.id})")
    game = discord.Game(name="!help for list of commands")
    await bot.change_presence(activity=game)

@bot.event
async def on_command_error(ctx,error):
    if(ctx.message.author != bot.user):
        print(f"{ctx.message.author} tried to use {ctx.message.content} command on server: {ctx.message.guild.name} in the channel: {ctx.message.channel.name}")

@bot.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author
    message = "**Hello! Thanks for using my bot!** \n" \
              "**Here are the list of commands you can use:** \n" \
              "\t**!dog** - This command will make me send out a random picture of a dog maybe cat? \n" \
              "\t**!games** - This command will let you pick from a variety of games I have including TicTacToe!, uhh that's it for now, Tommy is very lazy. \n \t \t    ConnectFour will be comming soon-ish.. 2022\n" \
              "\t**!clearchat (integer)** - This command will let you clear the chat of previous messages. Ex. !clear 10, will clear 10 messages \n" \
              "\t**!restart** - This command is very powerful... It will restart me, I might never come back online. Well you killed me. I hope you're happy. \n" \
              "\t**!pickup @user** - This command will send a random cheesy pickupline to a person of your choice :) \n" \
              "\t**!jokes** - This command will send a random darkjoke.. cough cough brought to you by Kelly\n" \
              "\t**!elmo** - This command will send a elmo picture... poop?.. cough cough brought to you by Nathan\n" \
              "\t**!ricepurity** - This command will send a random number from 0 to 100.. cough cough brought to you by Nathan\n" \
              "\t**!iq** - This command will send a random number from 0 to 200.. cough cough brought to you by Nathan\n" \
              "\t**!magicballs** - This command will send a random responds\n" \
              "\tIf you would like to play music. Please @thomaz because only he will have the power to turn that on. Basically It means that he can't have that running 24/7 \n" \
              "\t Think of his electric bill will you... He already has to keep me alive."
    await author.send(message)
    sendLogs(ctx);
def sendLogs(ctx):
    print(f"{ctx.message.author} used {ctx.message.content} command on server: {ctx.message.guild.name} in the channel: {ctx.message.channel.name}")


# plays out al ist
@bot.command()
async def games(ctx):
    print(f"{ctx.message.author} used {ctx.message.content} command on server: {ctx.message.guild.name} in the channel: {ctx.message.channel.name}")
    embed = discord.Embed(
        title= "Here is a List of Games: \n"
    )
    for games in (LIST_OF_GAMES):
        embed.add_field(name=games,value="\u200b")
    await ctx.message.add_reaction('✅')
    msg = await ctx.send(embed=embed)
    await msg.add_reaction("1️⃣")
    await msg.add_reaction("2️⃣")

    def check(reaction, user):
        return user != bot.user and (str(reaction.emoji) == "1️⃣" or "2️⃣")

    def checkemoji(reaction, user):
        return user != bot.user

    reaction, user = await bot.wait_for("reaction_add", timeout=30.0, check=check)
    if str(reaction.emoji) == "1️⃣":
        await ctx.send("Player 1: Pick your character! (React with an emoji)")
        reaction, user = await bot.wait_for("reaction_add",timeout=30.0, check=checkemoji)
        user_1_char = str(reaction.emoji)
        await ctx.send("Player 2: Pick your character! (React with an emoji)")
        reaction, user = await bot.wait_for("reaction_add", timeout=30.0, check=checkemoji)
        user_2_char = str(reaction.emoji)

        await ctx.channel.purge(limit=4)
        turn = 0
        while check_win(user_1_char, user_2_char) == BLANK and turn <= 9:
            await ctx.channel.purge(limit=2)
            await ctx.send(print_game_board(user_1_char,user_2_char))
            player1_turn_message = await ctx.send(f"Player {user_1_char}'s turn:")
            for x in range(len(onetonine)):
                await player1_turn_message.add_reaction(onetonine[x])
            reaction, user = await bot.wait_for("reaction_add", timeout=30.0, check=checkemoji)
            if str(reaction.emoji) == "❗":
                turn = 9
            give_move(str(reaction.emoji),user_1_char)
            remove_icon(onetonine,str(reaction.emoji))
            turn += 1
            if check_win(user_1_char, user_2_char) == BLANK and turn <= 9:
                await ctx.channel.purge(limit=2)
                await ctx.send(print_game_board(user_1_char, user_2_char))
                player2_turn_message = await ctx.send(f"Player {user_2_char}'s turn:")
                for x in range(len(onetonine)):
                    await player2_turn_message.add_reaction(onetonine[x])
                reaction, user = await bot.wait_for("reaction_add", timeout=30.0, check=checkemoji)

                if str(reaction.emoji) == "❗":
                    turn = 9
                give_move(str(reaction.emoji), user_2_char)
                remove_icon(onetonine, str(reaction.emoji))
                turn += 1

            print(GAME_BOARD)

        await ctx.channel.purge(limit=2)
        await ctx.send(print_game_board(user_1_char,user_2_char))
        if (check_win(user_1_char,user_2_char) == user_1_char):
            await ctx.send(f"Player {user_1_char} has won!")
        elif (check_win(user_1_char,user_2_char) == user_2_char):
            await ctx.send(f"Player {user_2_char} has won!")
        else:
            await ctx.send(f"It was a tie!")
        reset_board(GAME_BOARD)
        print(onetonine)
        reset_icons(onetonine)
        print(GAME_BOARD)

    elif str(reaction.emoji) == "2️⃣":
        await ctx.send("Please wait until 2022")




# restarting command to restart bot incase of new code.
@bot.command(pass_context=True, aliases=['r'])
async def restart(ctx):
    embed = discord.Embed(
        title=f"{bot.user.name} Restarting!",
    )
    embed.set_author(
        name=ctx.author.name,
        icon_url=ctx.author.avatar_url
    )
    await ctx.message.add_reaction('✅')
    await ctx.send(embed=embed)
    print(f"{ctx.message.author} used {ctx.message.content} command on server: {ctx.message.guild.name} in the channel: {ctx.message.channel.name}")
    await bot.close()

@bot.command(pass_context=True)
async def dog(ctx):
    await ctx.send(sendDogsLinks())
    sendLogs(ctx);

@bot.command(pass_context=True)
async def twerk(ctx):
    await ctx.send(sendTwerking())
    sendLogs(ctx);

@bot.command(pass_context=True)
async def pickup(ctx, user: discord.User):
    msg = sendRandomPickupLines()
    await ctx.channel.purge(limit=(int(1)))
    await user.send(msg)
    await user.send(f"Sent by {ctx.author.name}")
    sendLogs(ctx);
    print(f"{msg}")

@bot.command(pass_context=True)
async def jokes(ctx):
    await ctx.send(sendDarkJokes())
    sendLogs(ctx);



@bot.command(pass_context=True)
async def elmo(ctx):
    await ctx.send("https://imgur.com/xLFdpQk")
    sendLogs(ctx);

@bot.command(pass_context=True)
async def ricepurity(ctx):
    author = str(ctx.message.author)
    if author == "potato-uwu#1161":
        randomNum = random.randint(0, 15)
    elif author == "Thomaz#3972":
        randomNum = random.randint(80, 100)
    elif author == "Huiyene#5760":
        randomNum = random.randint(-100, 1)
    else:
        randomNum = random.randint(0, 100)
    await ctx.send(f"Your RicePurity is: {randomNum}")
    sendLogs(ctx);

@bot.command(pass_context=True)
async def iq(ctx):
    author = str(ctx.message.author)
    print("IQ!")
    iq = 0
    if(author != "Thomaz#3972"):
        iq = random.randint(0,189)
    else:
        iq = random.randint(180,200)
        print(iq)
    if(iq >= 0 and iq < 25):
        await ctx.send(f"Your IQ is: {iq}, \"{getIQScore(1)}\"")
    elif(iq >= 25 and iq < 35):
        await ctx.send(f"Your IQ is: {iq}, \"{getIQScore(2)}\"")
    elif (iq >= 35 and iq < 45):
        await ctx.send(f"Your IQ is: {iq}, \"{getIQScore(3)}\"")
    elif (iq >= 45 and iq < 60):
        await ctx.send(f"Your IQ is: {iq}, \"{getIQScore(4)}\"")
    elif (iq >= 60 and iq < 80):
        await ctx.send(f"Your IQ is: {iq}, \"{getIQScore(5)}\"")
    elif (iq >= 80 and iq < 95):
        await ctx.send(f"Your IQ is: {iq}, \"{getIQScore(6)}\"")
    elif (iq >= 95 and iq < 105):
        await ctx.send(f"Your IQ is: {iq}, \"{getIQScore(7)}\"")
    elif (iq >= 105 and iq < 115):
        await ctx.send(f"Your IQ is: {iq}, \"{getIQScore(8)}\"")
    elif (iq >= 115 and iq < 125):
        await ctx.send(f"Your IQ is: {iq}, \"{getIQScore(9)}\"")
    elif (iq >= 125 and iq < 140):
        await ctx.send(f"Your IQ is: {iq}, \"{getIQScore(10)}\"")
    elif (iq >= 140 and iq < 150):
        await ctx.send(f"Your IQ is: {iq}, \"{getIQScore(11)}\"")
    elif (iq >= 150 and iq < 160):
        await ctx.send(f"Your IQ is: {iq}, \"{getIQScore(12)}\"")
    elif (iq >= 160 and iq < 180):
        await ctx.send(f"Your IQ is: {iq}, \"{getIQScore(13)}\"")
    elif (iq >= 190 and iq < 200):
        await ctx.send(f"Your IQ is: {iq}, \"{getIQScore(14)}\"")



@bot.command(pass_context=True)
async def magicballs(ctx,phrase: str):
    if phrase == "is tommy amazing":
        await ctx.send("Yes, tommy is amazing. he is the best in the world. please help me.")
    elif phrase == "is tommy cool":
        await ctx.send("Yes he is the coolest, dear god save me, super cool")
    elif phrase == "is anh cool":
        await ctx.send("no. god no.")
    elif phrase == "is nathan cool":
        await ctx.send("ehh maybe? idk he seems kinda lame")
    else:
        await ctx.send(f"{sendmagicballs()}")
    sendLogs(ctx);

@bot.command(pass_context=True)
async def clearchat(ctx,amount: str):
    if amount == "all":
        await ctx.channel.purge()
    else:
        await ctx.channel.purge(limit=(int(amount) + 1))
    channel = discord.utils.get(ctx.guild.text_channel)
    sendLogs(ctx);


bot.run(TOKEN, bot=True, reconnect=True)

