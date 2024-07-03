import discord
from discord.ext import commands
from discord import app_commands
from useful_things.pit_functions import calcBracketColor
from useful_things.api_functions import getInfo
from useful_things.discord_functions import footerDateGen


class pitpandaSignatures(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    # Create the PitPanda prestige and level embed command
    @app_commands.command(name="prestige-level", description="Displays Pitpanda prestige and level signature")
    async def prestige_level(self, interaction: discord.Interaction, player: str):
        """my command description
        Args:
            player (str): A Minecraft username
        """
        pass

        urlPP: str = f"https://pitpanda.rocks/api/players/{player}"
        dataPP = getInfo(urlPP)

        if not dataPP["success"]:
            embedFail = discord.Embed(title="Player not found", color=discord.Color.red())

            await interaction.response.send_message(embed=embedFail, ephemeral=True)  # noqa
        else:
            currentPrestige = len(dataPP["data"]["prestiges"]) - 1

            embed = discord.Embed(title="Prestige & Level", color=calcBracketColor(int(currentPrestige)))
            embed.set_footer(text=footerDateGen())
            embed.set_image(url=f"https://pitpanda.rocks/api/images/level/{player}")

            await interaction.response.send_message(embed=embed)  # noqa

    # Create the PitPanda profile embed command
    @app_commands.command(name="profile", description="Display Pitpanda Profile Signature")
    async def profile(self, interaction: discord.Interaction, player: str):
        """my command description
        Args:
            player (str): A Minecraft username
        """
        pass

        urlPP: str = f"https://pitpanda.rocks/api/players/{player}"
        dataPP = getInfo(urlPP)

        if not dataPP["success"]:
            embedFail = discord.Embed(title="Player not found", color=discord.Color.red())

            await interaction.response.send_message(embed=embedFail, ephemeral=True)  # noqa
        else:
            currentPrestige = len(dataPP["data"]["prestiges"]) - 1

            embed = discord.Embed(title="Prestige & Level", color=calcBracketColor(int(currentPrestige)))
            embed.set_footer(text=footerDateGen())
            embed.set_image(url=f"https://pitpanda.rocks/api/images/profile/{player}")

            await interaction.response.send_message(embed=embed)  # noqa


async def setup(client: commands.Bot) -> None:
    await client.add_cog(pitpandaSignatures(client))
