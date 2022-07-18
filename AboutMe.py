@bot.slash_command(description="Bot information")
async def botinfo(interaction: Interaction):
    aboutme = nextcord.Embed(title=f"{bot.user.name} Information", description="""
    
MiniBoy is a discord bot created on August 01, 2021 as a test bot created by Ad. 
Then we were improving the bot to a point that we decided to publish it on top.gg. 
From there we hosted the bot and made it grow to a point where we reached 50 servers in no time. 
Until today we are and will be making constant updates to bring new features to the bot and improve it. 
Now the bot is undergoing a lot of updates that improve the bot and the user experience.

    """, color=0xf1c40f)
    await interaction.response.send_message(embed=aboutme)
