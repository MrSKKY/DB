from discord.ext import commands
from db import set_guild_config, update_guild_message, update_guild_channel

class ConfigCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='setprefix')
    @commands.has_permissions(administrator=True)
    async def setprefix(self, ctx, prefix: str):
        set_guild_config(ctx.guild.id, prefix)
        await ctx.send(f'Prefix set to: {prefix}')

    @commands.command(name='setjoinmessage')
    @commands.has_permissions(administrator=True)
    async def setjoinmessage(self, ctx, *, message: str):
        update_guild_message(ctx.guild.id, 'join_message', message)
        await ctx.send('Join message set.')

    @commands.command(name='setleavemessage')
    @commands.has_permissions(administrator=True)
    async def setleavemessage(self, ctx, *, message: str):
        update_guild_message(ctx.guild.id, 'leave_message', message)
        await ctx.send('Leave message set.')

    @commands.command(name='setbotmessage')
    @commands.has_permissions(administrator=True)
    async def setbotmessage(self, ctx, *, message: str):
        update_guild_message(ctx.guild.id, 'bot_message', message)
        await ctx.send('Bot message set.')

    @commands.command(name='setjoinchannel')
    @commands.has_permissions(administrator=True)
    async def setjoinchannel(self, ctx, channel_id: int):
        update_guild_channel(ctx.guild.id, 'join_channel', channel_id)
        await ctx.send(f'Join channel set to: {channel_id}')

    @commands.command(name='setleavechannel')
    @commands.has_permissions(administrator=True)
    async def setleavechannel(self, ctx, channel_id: int):
        update_guild_channel(ctx.guild.id, 'leave_channel', channel_id)
        await ctx.send(f'Leave channel set to: {channel_id}')

    @commands.command(name='setbotchannel')
    @commands.has_permissions(administrator=True)
    async def setbotchannel(self, ctx, channel_id: int):
        update_guild_channel(ctx.guild.id, 'bot_channel', channel_id)
        await ctx.send(f'Bot channel set to: {channel_id}')

def setup(bot):
    bot.add_cog(ConfigCog(bot))
