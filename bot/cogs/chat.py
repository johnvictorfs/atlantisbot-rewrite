# Standard lib imports
import time

# Non-Standard lib imports
import discord
from discord.ext import commands
import rs3clans

# Local imports
import definesettings as setting


def check_role(ctx, *roles):
    for role in roles:
        if role in str(ctx.message.author.roles):
            return True
    return False


class ChatCommands:

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['role', 'membro', 'Role', 'ROLE'])
    async def aplicar_role(self, ctx):
        await ctx.trigger_typing()
        print(f"> {ctx.author} issued command 'aplicar_role'.")
        start_time = time.time()

        role_message = (f"Informe seu usuário in-game.\n\n"
                        f"{setting.MOD_ID} {setting.ADMIN_ID} "
                        f"- O(a) Senhor(a) acima deseja receber um cargo acima de Convidado. Favor verificar :)")

        denied_message = "Fool! Você não é um Convidado!"

        if check_role(ctx, "Convidado"):
            await ctx.send(role_message)
        else:
            await ctx.send(denied_message)
        print(f"    - Answer sent. Took {time.time() - start_time:.4f}")

    @commands.command(aliases=['aplicar', 'raids'])
    async def aplicar_raids(self, ctx):
        await ctx.trigger_typing()
        print(f"> {ctx.author} issued command 'aplicar_raids'.")
        start_time = time.time()

        channel = setting.RAIDS_NOTIF_CHAT_ID
        raids_channel = "<#393104367471034369>"
        raids_chat = setting.RAIDS_CHAT_ID
        right_arrow = setting.MESSAGES["emoji"]["arrow_emoji"]

        aplicar_message = f"""
Olá! Você aplicou para receber a tag de Raids e participar dos Raids do Clã.

Favor postar uma screenshot que siga ao máximo possível as normas que estão escritas no topo do canal {raids_channel}
Use a imagem a seguir como base: <https://i.imgur.com/M4sU24s.png>

**Inclua na screenshot:**
 {right_arrow} Aba de `Equipamento` que irá usar
 {right_arrow} Aba de `Inventário` que irá usar
 {right_arrow} **`Perks de todas as suas Armas e Armaduras que pretende usar`**
 {right_arrow} `Stats`
 {right_arrow} `Barra de Habilidades` no modo de combate que utiliza
 {right_arrow} `Nome de usuário in-game`

Aguarde uma resposta de um {setting.RAIDS_TEACHER_ID}.

***Exemplo:*** https://i.imgur.com/CMNzquL.png"""

        denied_message = "Fool! Você já tem permissão para ir Raids!"

        if check_role(ctx, "Raids"):
            await ctx.send(denied_message)
        else:
            await ctx.send(aplicar_message)
        print(f"    - Answer sent. Took {time.time() - start_time:.4f}")

    @commands.command(aliases=['aplicaraod', 'aod', 'aodaplicar', 'aod_aplicar'])
    async def aplicar_aod(self, ctx):
        await ctx.trigger_typing()
        print(f"> {ctx.author} issued command 'aplicar_aod'.")
        start_time = time.time()

        aod_channel = "<#499740247647846401>"
        aod_teacher = "<@&346107676448522240>"
        aod_tag = "<@&499739627339382825>"
        right_arrow = setting.MESSAGES["emoji"]["arrow_emoji"]

        aplicar_message = f"""
Olá! Você aplicou para receber a tag de AoD e participar dos times de Nex: AoD do Clã.

Favor postar uma screenshot que siga ao máximo possível as normas que estão escritas no topo do canal {aod_channel}
Use a imagem a seguir como base:

Inclua na screenshot:
 {right_arrow} Aba de Equipamento que irá usar
 {right_arrow} Aba de Inventário que irá usar
 {right_arrow} Perks de todas as suas Armas e Armaduras que pretende usar
 {right_arrow} Stats
 {right_arrow} Barra de Habilidades no modo de combate que utiliza
 {right_arrow} Nome de usuário in-game

Aguarde uma resposta de um {aod_teacher}.

***Exemplo (Aplicação para Raids):*** https://i.imgur.com/CMNzquL.png"""

        denied_message = "Fool! Você já tem permissão para ir nos times de AoD!"

        if check_role(ctx, "Angel of Memes", "Aod"):
            await ctx.send(denied_message)
        else:
            await ctx.send(aplicar_message)
        print(f"    - Answer sent. Took {time.time() - start_time:.4f}")

    @commands.command(aliases=['git', 'source'])
    async def github(self, ctx):
        await ctx.trigger_typing()
        print(f"> {ctx.author} issued command 'github'.")
        start_time = time.time()

        github_icon = "https://assets-cdn.github.com/images/modules/logos_page/GitHub-Mark.png"
        repo_url = "https://github.com/johnvictorfs/atlantisbot-rewrite"
        johnvictorfs_img = "https://avatars1.githubusercontent.com/u/37747572?s=460&v=4"
        johnvictorfs_url = "https://github.com/johnvictorfs"

        github_embed = discord.Embed(title="atlantisbot-rewrite",
                                     description="",
                                     color=discord.Colour.dark_blue(),
                                     url=repo_url)
        github_embed.set_author(icon_url=johnvictorfs_img,
                                url=johnvictorfs_url, name="johnvictorfs")
        github_embed.set_thumbnail(url=github_icon)

        await ctx.send(content=None, embed=github_embed)
        print(f"    - Answer sent. Took {time.time() - start_time:.4f}")

    @commands.command(aliases=['atlbot', 'atlbotcommands'])
    async def atlcommands(self, ctx):
        await ctx.trigger_typing()
        print(f"> {ctx.author} issued command 'atlcommands'.")
        start_time = time.time()

        runeclan_url = f"https://runeclan.com/clan/{setting.CLAN_NAME}"
        clan_banner_url = f"http://services.runescape.com/m=avatar-rs/l=3/a=869/{setting.CLAN_NAME}/clanmotif.png"
        embed_title = "RuneClan"

        atlcommands_embed = discord.Embed(title=embed_title,
                                          description="",
                                          color=discord.Colour.dark_blue(),
                                          url=runeclan_url,
                                          )
        atlcommands_embed.set_author(
            icon_url=clan_banner_url, name="AtlantisBot")
        atlcommands_embed.set_thumbnail(
            url="http://rsatlantis.com/images/logo.png")

        atlcommands_embed.add_field(name=f"{setting.PREFIX}claninfo <nome de jogador>",
                                    value="Ver info de Clã de Jogador",
                                    inline=False)
        atlcommands_embed.add_field(name=f"{setting.PREFIX}raids",
                                    value="Aplicar para ter acesso aos Raids do Clã",
                                    inline=False)
        atlcommands_embed.add_field(name=f"{setting.PREFIX}role",
                                    value="Aplicar para receber o role de Membro no Discord",
                                    inline=False)
        atlcommands_embed.add_field(name=f"{setting.PREFIX}comp <número da comp.> <número de jogadores>",
                                    value="Ver as competições ativas do Clã",
                                    inline=False)
        atlcommands_embed.add_field(name=f"{setting.PREFIX}github",
                                    value="Ver o repositório desse bot no Github",
                                    inline=False)
        atlcommands_embed.add_field(name=f"{setting.PREFIX}atlcommands",
                                    value="Ver essa mensagem",
                                    inline=False)
        atlcommands_embed.set_footer(text="Criado por @NRiver#2263")

        await ctx.send(embed=atlcommands_embed)
        print(f"    - Answer sent. Took {time.time() - start_time:.4f}")

    @commands.command(aliases=['ranksupdate', 'upranks'])
    async def ranks(self, ctx):
        await ctx.trigger_typing()
        exp_general = 500_000_000
        exp_captain = 225_000_000
        exp_lieutenant = 125_000_000
        exp_seargent = 50_000_000

        rank_emoji = {
            'Corporal': setting.CLAN_SETTINGS['Corporal']['Emoji'],
            'Sergeant': setting.CLAN_SETTINGS['Sergeant']['Emoji'],
            'Lieutenant': setting.CLAN_SETTINGS['Lieutenant']['Emoji'],
            'Captain': setting.CLAN_SETTINGS['Captain']['Emoji'],
            'General': setting.CLAN_SETTINGS['General']['Emoji'],
        }

        ranks_embed = discord.Embed(title="__Ranks a Atualizar__",
                                    description=" ",)
        found = False
        clan = rs3clans.Clan(setting.CLAN_NAME, set_exp=False)
        for member in clan.member.items():
            if member[1]['exp'] >= exp_general and member[1]['rank'] == 'Captain':
                ranks_embed.add_field(name=member[0],
                                      value=f"Capitão {rank_emoji['Captain']} > General {rank_emoji['General']}\n**__Exp:__** {member[1]['exp']:,}\n" + (
                                          "_\\" * 15) + "_",
                                      inline=False)
                found = True
            elif member[1]['exp'] >= exp_captain and member[1]['rank'] == 'Lieutenant':
                ranks_embed.add_field(name=member[0],
                                      value=f"Tenente {rank_emoji['Lieutenant']} > Capitão {rank_emoji['Captain']}\n**__Exp:__** {member[1]['exp']:,}\n" + (
                                          "_\\" * 15) + "_",
                                      inline=False)
                found = True
            elif member[1]['exp'] >= exp_lieutenant and member[1]['rank'] == 'Sergeant':
                ranks_embed.add_field(name=member[0],
                                      value=f"Sargento {rank_emoji['Sergeant']} > Tenente {rank_emoji['Lieutenant']}\n**__Exp:__** {member[1]['exp']:,}\n" + (
                                          "_\\" * 15) + "_",
                                      inline=False)
                found = True
            elif member[1]['exp'] >= exp_seargent and member[1]['rank'] == 'Corporal':
                ranks_embed.add_field(name=member[0],
                                      value=f"Cabo {rank_emoji['Corporal']} > Sargento {rank_emoji['Sergeant']}\n**__Exp:__** {member[1]['exp']:,}\n" + (
                                          "_\\" * 15) + "_",
                                      inline=False)
                found = True
        if not found:
            ranks_embed.add_field(name="Nenhum Rank a ser atualizado no momento :)",
                                  value=("_\\" * 15) + "_",
                                  inline=False)
        await ctx.send(embed=ranks_embed)


def setup(bot):
    bot.add_cog(ChatCommands(bot))
