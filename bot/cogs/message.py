from discord.ext import commands
from db import get_guild_config

class MessageCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        guild_config = get_guild_config(message.guild.id)
        prefix = guild_config['prefix'] if guild_config else '!'

        if message.content.startswith(prefix):
            await self.bot.process_commands(message)
            bot_message = guild_config['bot_message']
            if bot_message:
                bot_channel_id = guild_config['bot_channel']
                if bot_channel_id:
                    bot_channel = self.bot.get_channel(bot_channel_id)
                    if bot_channel:
                        await bot_channel.send(bot_message)
                    else:
                        await message.channel.send(bot_message)
                else:
                    await message.channel.send(bot_message)

def setup(bot):
    bot.add_cog(MessageCog(bot))
