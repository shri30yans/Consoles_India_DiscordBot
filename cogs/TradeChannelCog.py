import discord
from discord.ext import commands
import config
from io import BytesIO


class TradeChannel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # @commands.Cog.listener()
    # async def on_raw_reaction_add(self,payload):
    #     channel = self.bot.get_channel(payload.channel_id)
    #     user = self.bot.get_user(payload.user_id)
    #     message = await channel.fetch_message(payload.message_id)
    #     emoji=payload.emoji
    #     if message.id == config.ticket

    @commands.has_permissions(manage_channels=True)
    @commands.bot_has_permissions(manage_channels=True)
    @commands.command(
        name="CreateTradeChannel",
        aliases=["ctc"],
        help=f"Creates a trade channel.",
        require_var_positional=True,
    )  # require_var_positional=True makes sure input is not empty
    async def CreateTradeChannel(
        self,
        ctx,
        members: commands.Greedy[discord.Member],
        trade_number="",
        *,
        description="Trade Channel",
    ):
        if ctx.guild.id == config.playstation_server_id:
            admin_role = ctx.guild.get_role(config.admin_role_id)
            head_moderator_role = ctx.guild.get_role(config.head_moderator_role_id)
            moderator_role = ctx.guild.get_role(config.moderator_role_id)
            game_trade_moderator_role = ctx.guild.get_role(
                config.game_trade_moderator_role_id
            )
            bot_role = ctx.guild.get_role(config.bot_role_id)

            overwrites = {
                admin_role: discord.PermissionOverwrite(
                    send_messages=True,
                    read_messages=True,
                ),  # read_message_history=True,use_external_emojis=True,attach_files=True,embed_links=True),
                head_moderator_role: discord.PermissionOverwrite(
                    send_messages=True, read_messages=True
                ),
                moderator_role: discord.PermissionOverwrite(
                    send_messages=True, read_messages=True
                ),
                game_trade_moderator_role: discord.PermissionOverwrite(
                    send_messages=True, read_messages=True
                ),
                bot_role: discord.PermissionOverwrite(
                    send_messages=True, read_messages=True
                ),
                ctx.guild.default_role: discord.PermissionOverwrite(
                    read_messages=False
                ),
            }

            member_names = ""
            for mbr in members:
                if mbr == ctx.author:
                    pass

                elif mbr.bot:
                    pass

                else:
                    overwrites[mbr] = discord.PermissionOverwrite(
                        send_messages=True, read_messages=True
                    )
                    try:
                        member_names += mbr.mention + " "
                    except:
                        try:
                            member_names += mbr.name + " "
                        except:
                            pass

            if member_names == "":
                member_names = "No members were added to this Trade."
            else:
                pass

            category = self.bot.get_channel(config.trade_category_id)
            channel = await category.create_text_channel(
                f"trade {trade_number}",
                overwrites=overwrites,
                topic=description,
                reason="Trade Channel",
            )
            embed = discord.Embed(
                title=f"Trade channel created.",
                description=f"{channel.mention} \nMember's added to trade: {member_names} \nDescription: {description}",
            )
            embed.set_footer(
                icon_url=ctx.author.display_avatar.url,
                text=f"Requested by {ctx.message.author} • {self.bot.user.name} ",
            )
            await ctx.send(embed=embed)
            embed = discord.Embed(
                title=f"Trade instructions",
            )
            embed.add_field(
                name="Process",
                value="""1) The buyer sends the money to a Games Trades Moderator.\n2) The seller will then ship the product and send tracking details to the buyer.\n3) The buyer upon receiving the product checks the conditions of the product.\n4) Once the buyer is satisfied with the product a Games Trades Moderator will transfer money to the seller.""",
                inline=False,
            )
            embed.add_field(
                name="Seller Instructions",
                value="Confirm the product and its price before proceeding further.",
                inline=False,
            )
            embed.add_field(
                name="Buyer Instructions",
                value="Check with the selling party before transferring the amount to a Game Trade Moderator. Make sure to collect the tracking ID after the seller has shipped the product.",
                inline=False,
            )
            embed.add_field(
                name="Miscellaneous",
                value="[Shipping Tips](https://discord.com/channels/797570077364977696/815188535907975198/815469791032508416)",
                inline=False,
            )
            embed.set_footer(
                icon_url=ctx.author.display_avatar.url,
                text=f"Requested by {ctx.message.author} • {self.bot.user.name} ",
            )
            message = await channel.send(
                embed=embed,
                content=f"{member_names} Here is the requested channel. A {game_trade_moderator_role.mention} will be here to coordinate with you soon.",
            )
            await message.add_reaction("\U0001f44d")  # thumbs up

        else:
            await ctx.send(
                "You can't use this command in this server. Use this command in a Approved Server."
            )

    @commands.has_permissions(manage_messages=True)
    @commands.bot_has_permissions(manage_channels=True)
    @commands.command(
        name="CloseTradeChannel",
        aliases=["close", "closetrade"],
        help=f"Closes a trade channel and creates a log. Can be in `.html` or `.txt`. Format can be HTML or TXT.",
    )  # require_var_positional=True makes sure input is not empty
    async def CloseTradeChannel(self, ctx, type: str = "txt"):
        if ctx.guild.id == config.playstation_server_id:
            if "trade" in ctx.channel.name:

                if type.lower() in ["text", "txt", ".txt"]:
                    channel = self.bot.get_channel(config.mod_logs_channel_id)
                    embed = discord.Embed(
                        Title="Fetching messages...",
                        description="Fetching messages to create a transcript. Please wait.",
                    )
                    message = await ctx.send(embed=embed)
                    messages = await ctx.channel.history(limit=1000).flatten()
                    text = "▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬"
                    text += f"""\n{channel.name.title()} transcript\nServer: {ctx.guild.name} ({ctx.guild.id})\nChannel: {ctx.channel.name} \nMessages: {len(messages)} \n"""
                    messages_string = ""
                    users_in_channel = ""
                    # admin_role=ctx.guild.get_role(config.admin_role_id)
                    # head_moderator_role=ctx.guild.get_role(config.head_moderator_role_id)
                    # moderator_role=ctx.guild.get_role(config.moderator_role_id)
                    # game_trade_moderator_role=ctx.guild.get_role(config.game_trade_moderator_role_id)
                    # async def if_moderator(member):
                    #     for x in member.roles:
                    #         if x in [admin_role,head_moderator_role,moderator_role,game_trade_moderator_role]:
                    #             return True
                    #         else:
                    #             return False

                    for msg in messages[::-1]:
                        if msg.author.bot:
                            # bot messages will not come in the transcript
                            pass
                        else:
                            messages_string += f"{msg.author.name}: {msg.content} \n"

                        if str(msg.author.id) not in users_in_channel and not (
                            msg.author.bot
                        ):
                            users_in_channel += (
                                f"\u2800\u2800{msg.author.name} ({msg.author.id})\n"
                            )

                    text += "User's in this channel:\n" + users_in_channel
                    text += "▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n"
                    text += messages_string

                    buffer = BytesIO(
                        text.encode("utf8")
                    )  # change encoding as necessary
                    await channel.send(
                        content=f"Trade transcript of {ctx.channel.name}",
                        file=discord.File(
                            fp=buffer,
                            filename=f"{ctx.channel.name.upper()}_transcript.txt",
                        ),
                    )
                    embed = discord.Embed(
                        title="Transcript created.",
                        description=f"A `.txt` transcript has been sent to {channel.mention}.\nThis channel can now be deleted.",
                    )
                    # embed.add_field(name="Users",value=user_string)
                    await message.edit(embed=embed)

                elif type.lower() in ["html", ".html"]:
                    channel = self.bot.get_channel(config.mod_logs_channel_id)
                    embed = discord.Embed(
                        title="Fetching messages...",
                        description="Fetching messages to create a transcript. Please wait.",
                    )
                    message = await ctx.send(embed=embed)
                    messages = await ctx.channel.history(limit=1000).flatten()
                    text = f"""<html><head><title>{channel.name} transcript</title></head><div class=header"><img src="{ctx.guild.icon_url}" alt="{ctx.guild.name} logo" height="200px" width ="200px"/><h2><b>Server:</b> {ctx.guild.name} ({ctx.guild.id})<br><b>Channel:</b> {ctx.channel.name} <br><b>Messages:</b> {len(messages)} \n</h2></div><br><body>"""
                    # users={}
                    for msg in messages[::-1]:
                        if (
                            msg.author.bot
                        ):  # bot messages will not come in the transcript
                            pass
                        else:
                            text += f"<b>{msg.author.name}</b>: {msg.content}<br>"
                            # if msg.author.id in users.keys():
                            #     users[msg.author.id]+=1
                            # else:
                            #     users[msg.author.id]=1

                    # People who spoke in transcript
                    # user_string,user_transcript_string="",""
                    # for user_id in users:
                    #     user=self.bot.get_user(user_id)
                    #     user_string+=f"{user.mention} : {users[user]} Messages \n"
                    #     user_transcript_string+=f"{user.name} : {users[user]} Messages <br>"

                    # text+=f"<h2>Users: <br> {user_transcript_string}</h2>" + "</body></html>"
                    text += "</body></html>"
                    buffer = BytesIO(
                        text.encode("utf8")
                    )  # change encoding as necessary
                    await channel.send(
                        content=f"Trade transcript of {ctx.channel.name}",
                        file=discord.File(
                            fp=buffer, filename=f"{ctx.channel.name}_transcript.html"
                        ),
                    )

                    embed = discord.Embed(
                        title="Transcript created.",
                        description=f"A `.html` transcript has been sent to {channel.mention}.\n This channel can now be deleted.",
                    )
                    # embed.add_field(name="Users",value=user_string)
                    await message.edit(embed=embed)
            else:
                await ctx.send(
                    "You can't use this command in this channel. Use this command in a trade channel."
                )

        else:
            await ctx.send(
                "You can't use this command in this channel. Use this command in a trade channel."
            )

        # print(messages)
        # text = open("template.html","r",encoding='utf-8').read()
        # #print(text)
        # newfile = open("ticketlog.html","w")
        # newfile.write(text)


async def setup(bot):
    await bot.add_cog(TradeChannel(bot))
