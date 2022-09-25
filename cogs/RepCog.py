import discord
import random
from discord.ext import commands
import config


class RepCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="Rep", help=f"Shows the current rep")
    async def rep(self,ctx,user:discord.Member=None):
        user = user or ctx.author
        DatabaseFunctions = self.bot.get_cog('DatabaseFunctions')

        if user.bot:
            await ctx.reply(f"{user.name} is a bot. Bots don't have accounts.")
            return
        else:
            sent_msg = await ctx.reply(embed=discord.Embed(title=f"{config.loading_reaction}    {user.name}'s Rep",description=f"Fetching {user.name}'s inventory from the database...",colour = random.choice(config.embed_colours)))
            rep = await DatabaseFunctions.get_user_rep(user,str(ctx.guild.id))
            embed=discord.Embed(title=f"{user.name}'s Balance",colour = random.choice(config.embed_colours))
            embed.add_field(name="Rep",value=f"{rep}")
            embed.set_footer(icon_url= ctx.author.display_avatar.url,text=f"Requested by {ctx.message.author} • {self.bot.user.name}")
            await sent_msg.edit(embed=embed)
        
    @commands.command(name="Leaderboard",aliases=["lb"],help=f"Shows the server leaderboard according to the rep.")
    async def leaderboard(self,ctx,page:int=1):
        sent_msg = await ctx.reply(embed=discord.Embed(title=f"{config.loading_reaction}   Server Leaderboard",description=f"Fetching the server leaderboard...",colour = random.choice(config.embed_colours)))

        DatabaseFunctions = self.bot.get_cog('DatabaseFunctions')
        server_id = str(ctx.guild.id)
        formated_list = await DatabaseFunctions.get_leaderboard(server_id,offset=page*10-10)

        top=formated_list[page*10-10:page*10]
        top_string=""
        num = 0
        for entry in top:
            #num = formated_list.index(entry) + 1
            user = ctx.guild.get_member(entry["user_id"])
            if user:
                num += 1
                top_string = top_string + f"`{num}.` " + f" {user.mention}  •  `{entry[server_id]} Rep`" + "\n"

        
        if len(top_string) == 0:#is space/blank/None
            top_string = "There are no entries in your leaderboard."
        
        embed=discord.Embed(title=f"Rep Leaderboard",description=f"{top_string}",colour = random.choice(config.embed_colours))
        embed.set_footer(icon_url= ctx.author.display_avatar.url,text=f"Requested by {ctx.message.author} • {self.bot.user.name}")
        await sent_msg.edit(embed=embed)
    

    @commands.has_permissions(manage_roles=True)
    @commands.bot_has_permissions(manage_roles=True)
    @commands.command(name="SetRep", help=f"Sets the rep of a user")
    async def setrep(self,ctx,members: commands.Greedy[discord.Member],amt=1):
        sent_msg = await ctx.reply(embed=discord.Embed(title=f"{config.loading_reaction}    Setting Rep",description=f"Setting rep to {amt}...",colour = random.choice(config.embed_colours)))
        DatabaseFunctions = self.bot.get_cog('DatabaseFunctions')
        updated_users = ""
        for user in members:
            if user.bot:
                #await ctx.reply(f"{user.name} is a bot. Bots don't have accounts.")
                pass
            else:
                await DatabaseFunctions.set_user_rep(user,str(ctx.guild.id),amt)
                updated_users += f"{user.mention}, "
                
        embed=discord.Embed(title=f"Rep set.",colour = random.choice(config.embed_colours))
        embed.add_field(name="Rep was updated.",value=f"{updated_users}'s rep was updated.")
        embed.set_footer(icon_url= ctx.author.display_avatar.url,text=f"Requested by {ctx.message.author} • {self.bot.user.name}")
        await sent_msg.edit(embed=embed)
    

    
    @commands.has_permissions(manage_roles=True)
    @commands.bot_has_permissions(manage_roles=True)
    @commands.command(name="AddRep", help=f"Adds rep to a user")
    async def addrep(self,ctx,members: commands.Greedy[discord.Member],amt=1):
        sent_msg = await ctx.reply(embed=discord.Embed(title=f"{config.loading_reaction}    Adding Rep",description=f"Adding {amt} rep...",colour = random.choice(config.embed_colours)))
        DatabaseFunctions = self.bot.get_cog('DatabaseFunctions')
        updated_users = ""
        for user in members:
            if user.bot:
                #await ctx.reply(f"{user.name} is a bot. Bots don't have accounts.")
                pass
            else:
                await DatabaseFunctions.add_user_rep(user,str(ctx.guild.id),amt)
                updated_users += f"{user.mention}, "

        embed=discord.Embed(title=f"Rep added.",colour = random.choice(config.embed_colours))
        embed.add_field(name="Rep was updated.",value=f"{updated_users}'s rep was updated.")
        embed.set_footer(icon_url= ctx.author.display_avatar.url,text=f"Requested by {ctx.message.author} • {self.bot.user.name}")
        await sent_msg.edit(embed=embed)


                    

async def setup(bot):
    await bot.add_cog(RepCog(bot))