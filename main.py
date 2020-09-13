import discord
from discord.ext import commands
from discord.utils import get
import asyncio
from config import *
import datetime
from tictactoe import *

# makes a bot called "bot" with the "!" prefix
bot = commands.Bot(command_prefix=PREFIX, description="Personal Bot that plays games")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} and connected to Discord! (ID: {bot.user.id})")
    game = discord.Game(name="!play for list of games")
    await bot.change_presence(activity=game)


# plays out al ist
@bot.command()
async def play(ctx):
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
        return user == ctx.message.author and user != 'Personal Bot#5699' and (str(reaction.emoji) == "1️⃣" or "2️⃣")

    def checkemoji(reaction, user):
        return user == ctx.message.author and user != 'Personal Bot#5699'
    try:
        reaction, user = await bot.wait_for("reaction_add", timeout=30.0, check=check)
    except asyncio.TimeoutError:
        ctx.send("Timed out. Please do !play again if you want to play.")
    else:
        if str(reaction.emoji) == "1️⃣":
            await ctx.send("Player 1: Pick your character! (React with an emoji)")
            try:
                reaction, user = await bot.wait_for("reaction_add",timeout=30.0, check=checkemoji)
            except asyncio.TimeoutError:
                ctx.send("Timed out. Please do !play again if you want to play.")
            else:
                user_1_char = str(reaction.emoji)
                await ctx.send("Player 2: Pick your character! (React with an emoji)")
                try:
                    reaction, user = await bot.wait_for("reaction_add", timeout=30.0, check=checkemoji)
                except asyncio.TimeoutError:
                    ctx.send("Timed out. Please do !play again if you want to play.")
                else:
                    user_2_char = reaction.emoji
                    onetonine = ["1️⃣","2️⃣","3️⃣","4️⃣","5️⃣","6️⃣","7️⃣","8️⃣","9️⃣","❗"]
                    await ctx.channel.purge(limit=4)
                    turn = 0
                    while check_win(user_1_char, user_2_char) == BLANK and turn <= 9:
                        await ctx.channel.purge(limit=2)
                        await ctx.send(print_game_board(user_1_char,user_2_char))
                        player1_turn_message = await ctx.send(f"Player {user_1_char}'s turn:")
                        for x in range(10):
                            await player1_turn_message.add_reaction(onetonine[x])
                        try:
                            reaction, user = await bot.wait_for("reaction_add", timeout=30.0, check=checkemoji)
                        except asyncio.TimeoutError:
                            await ctx.send("Timed out. Please do !play again if you want to play.")
                        else:
                            if str(reaction.emoji) == "❗":
                                turn = 9
                            give_move(str(reaction.emoji),user_1_char)
                            turn += 1
                            if check_win(user_1_char, user_2_char) == BLANK and turn <= 9:
                                await ctx.channel.purge(limit=2)
                                await ctx.send(print_game_board(user_1_char, user_2_char))
                                player2_turn_message = await ctx.send(f"Player {user_2_char}'s turn:")
                                for x in range(10):
                                    await player2_turn_message.add_reaction(onetonine[x])
                                try:
                                    reaction, user = await bot.wait_for("reaction_add", timeout=30.0, check=checkemoji)
                                except asyncio.TimeoutError:
                                    await ctx.send("Timed out. Please do !play again if you want to play.")
                                else:
                                    if str(reaction.emoji) == "❗":
                                        turn = 9
                                    give_move(str(reaction.emoji), user_2_char)
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
                    print(GAME_BOARD)

        if str(reaction.emoji) == "2️⃣":
            msg = "bob"
            await ctx.send(msg)
            return

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
    await bot.close()


@bot.command(pass_context=True)
async def clear(ctx,amount: str):
    if amount == "all":
        await ctx.channel.purge()
    else:
        await ctx.channel.purge(limit=(int(amount) + 1))

bot.run(TOKEN, bot=True, reconnect=True)

