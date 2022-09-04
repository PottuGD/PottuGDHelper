import discord
import chalk
from discord.ext import commands


class Events(commands.Cog, name='Events', description='Events and triggers that run in the background.'):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(chalk.white('-------------------------------------------------------------'))
        print(chalk.green(f'>>| Logged in as {self.client.user} (ID: {self.client.user.id})'))
        print(chalk.white('-------------------------------------------------------------'))

    @commands.Cog.listener()
    async def on_message_delete(self, ctx: discord.ApplicationContext, message):
        return

    @commands.Cog.listener()
    async def on_command_error(self, ctx: discord.ApplicationContext, error):
        
        error_message = '\⛔ {}'.format(error)
        
        if isinstance(error, commands.CommandNotFound):
            return
        else:
            e = discord.Embed(
                description=error_message,
                color=discord.Color.dark_red()
            )
            await ctx.send(embed=e, mention_author=False)
            print(chalk.yellow(f'>>| {error}'))
            # raise error
        
        
def setup(client):
    client.add_cog(Events(client))
