# Standard lib imports
import os
import datetime
import traceback

# Non-Standard lib imports
import discord
from discord.ext import commands

# Local imports
from .utils import separator
import definesettings as setting


def check_role(ctx, *roles):
    for role in roles:
        if role in str(ctx.message.author.roles):
            return True
    return False


class TeamCommands:

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['maketeam', 'newteam', 'createteam'])
    async def team(self, ctx, title, team_size, channel=None, role=None):
        try:
            try:
                TEAM_ID = int(os.environ.get('TEAM_ID', "0"))
                if TEAM_ID == 0:
                    os.environ['TEAM_ID'] = str(1)
                else:
                    os.environ['TEAM_ID'] = str(TEAM_ID + 1)
                TEAM_ID += 1
            except Exception as e:
                await ctx.send("Erro inesperado. Contate ")
            print(f"$ Created Team '{title}' with TEAM_ID: {TEAM_ID} by '{ctx.author}'")
            if channel:
                try:
                    team_size = int(team_size)
                except ValueError:
                    return await ctx.send(f"Valor inválido: Tamanho de time ({team_size})")
                try:
                    channel_id = int(channel.replace('<', '').replace('#', '').replace('>', ''))
                except ValueError:
                    return await ctx.send(f"Valor inválido: Canal ({channel})")
                try:
                    input_channel = channel
                    channel = self.bot.get_channel(int(channel_id))
                    if not channel:
                        return await ctx.send(f"Valor inválido: Canal ({input_channel})")
                except Exception as e:
                    await ctx.send(e)
            else:
                channel = ctx.channel
            description = ""
            requisito = "\n"
            if role:
                description += f"Necessário: {role}"
                requisito = f"Requisito: {role}\n\n"
            if channel:
                description += f"\nMarque presença no: {channel.mention}"
            invite_embed = discord.Embed(
                title=f"Marque presença para '{title}' ({team_size} pessoas)",
                description=f"{separator}\nTime: {ctx.channel.mention}\n{requisito}"
                            f"`in {TEAM_ID}`: Marcar presença\n"
                            f"`out {TEAM_ID}`: Retirar presença"
            )
            embed_footer = f"Digite '{setting.PREFIX}del {TEAM_ID}' para excluir o time."
            team_embed = discord.Embed(
                title=f"__{title}__ - 0/{team_size}",
                description=description,
                color=discord.Color.purple()
            )
            team_embed.set_footer(
                text=embed_footer
            )
            await ctx.send(embed=team_embed)
            team_message = await ctx.channel.history().get(author=self.bot.user)
            await channel.send(embed=invite_embed)
            last_message = await channel.history().get(author=self.bot.user)
            invite_message = await channel.history().get(author=self.bot.user)
            finished = False
            team_list = []
            while not finished:
                async for message in channel.history(after=last_message):
                    if message.content.lower() == f'in {TEAM_ID}':
                        if message.author.bot:
                            await channel.send(f"`beep boop`\nHow do you do fellow human?")
                            continue
                        await message.delete()
                        roles = []
                        for role_ in message.author.roles:
                            roles.append(f"<@&{role_.id}>")
                        if role in roles or not role:
                            if message.author.mention in team_list:
                                await channel.send(f"Ei {message.author.mention}, você já está no time '{title}'! Não tente me enganar.")
                            elif len(team_list) >= int(team_size):
                                await channel.send(f"{message.author.mention}, o time '{title}' já está cheio!")
                            else:
                                await channel.send(f"{message.author.mention} foi adicionado ao time '{title}'.")
                                team_list.append(message.author.mention)
                        else:
                            no_perm_embed = discord.Embed(
                                title=f"__Permissões insuficientes__",
                                description=f"Você precisa ter o cargo {role} para entrar nesse time.",
                                color=discord.Color.dark_red()
                            )
                            await channel.send(content=message.author.mention, embed=no_perm_embed)
                    elif message.content.lower() == f'out {TEAM_ID}':
                        if message.author.bot:
                            await channel.send(f"`beep boop`\nHow do you do fellow human?")
                            continue
                        await message.delete()
                        if message.author.mention in team_list:
                            await channel.send(f"{message.author.mention} foi removido do time '{title}'.")
                            team_list.remove(message.author.mention)
                        else:
                            await channel.send(f"Ei {message.author.mention}, você já não estava no time '{title}'! Não tente me enganar.")
                    elif message.content.lower() == f'{setting.PREFIX}del {TEAM_ID}' and message.author == ctx.message.author:
                        print(f'$ Team \'{title}\' has been issued for deletion. ID: {TEAM_ID}')
                        await team_message.delete()
                        await ctx.message.delete()
                        await invite_message.delete()
                        return await message.delete()
                    last_message = message
                    async for message in ctx.channel.history(after=team_message):
                        if message.content.lower() == f'{setting.PREFIX}del {TEAM_ID}' and message.author == ctx.message.author:
                            print(f'$ Team \'{title}\' has been issued for deletion. ID: {TEAM_ID}')
                            await team_message.delete()
                            await ctx.message.delete()
                            await invite_message.delete()
                            return await message.delete()
                team_embed = discord.Embed(
                    title=f"__{title}__ - {len(team_list)}/{team_size}",
                    description=description,
                    color=discord.Color.purple()
                )
                team_embed.set_footer(
                    text=embed_footer
                )
                for index, member in enumerate(team_list):
                    team_embed.add_field(
                        name=separator,
                        value=f"{index + 1}- {member}",
                        inline=False
                    )
                try:
                    await team_message.edit(embed=team_embed)
                except discord.NotFound:
                    # This breaks out of the loop and ends the command if the team list message has been deleted
                    await ctx.message.delete()
                    break
        except Exception as e:
            logs_channel = self.bot.get_channel(int(setting.LOGS_CHANNEL))
            await logs_channel.send(f"""
Exception: `{e}`

Traceback:
```python
{traceback.print_exc()}
```

Command: `teams`

Author: `{ctx.author}`

Channel: `#{ctx.channel}`

**Arguments:**

`title::`
    {title}

`team_size::`
    {team_size}

`channel::`
    {channel}

`role::`
    {role}


DATE: `{datetime.datetime.now()}`
ID: `{TEAM_ID}`
""")


def setup(bot):
    bot.add_cog(TeamCommands(bot))