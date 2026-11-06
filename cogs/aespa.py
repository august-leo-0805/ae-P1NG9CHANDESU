import json
import os

import discord
from discord import app_commands
from discord.ext import commands

class Aespa(commands.Cog) :
    def __init__(self, bot) :
        self.bot = bot

        base_path = os.path.dirname(os.path.abspath(__file__))
        self.data_file = os.path.join(base_path, "..", "data/aespa_data.json")

        with open(self.data_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        self.aespa_data=data['aespa_data']

    async def send_sns(self, interaction: discord.Interaction, name):
        data = self.aespa_data[name]
        embed = discord.Embed(title = f"{data['emoji']} Be my æ, {name}'s SNS", color =0xc88ddd)

        if(name == "aespa"):
            embed.add_field(name = "Facebook", value = f"[바로가기](https://www.facebook.com/{data['facebook']})", inline = False)
            embed.add_field(name = "Instagram", value = f"[바로가기](https://www.instagram.com/{data['instagram']})", inline = False)
            embed.add_field(name = "Tiktok", value = f"[바로가기](https://www.tiktok.com/{data['tiktok']})",inline = False)
            embed.add_field(name = "Twitter", value = f"[바로가기](https://www.x.com/{data['twitter']})", inline = False)
            embed.add_field(name = "Weibo", value = f"[바로가기](https://weibo.com/u/{data['weibo']})", inline = False)            
            embed.add_field(name = "Youtube", value = f"[바로가기](https://www.youtube.com/{data['youtube']})", inline = False)

        elif name in ["karina", "giselle"] : 
            embed.add_field(name = "Instagram", value = f"[바로가기](https://www.instagram.com/{data['instagram']})", inline = False)

        elif name in ["winter"] : 
            embed.add_field(name = "Instagram", value = f"[바로가기](https://www.instagram.com/{data['instagram']})", inline = False)
            embed.add_field(name = "Pponyo's Instagram", value = f"[바로가기](https://www.instagram.com/{data['pponyo']})", inline = False)

        elif name == "ningning" :
            embed.add_field(name = "Instagram", value = f"[바로가기](https://www.instagram.com/{data['instagram']})", inline = False)
            embed.add_field(name = "Weibo", value = f"[바로가기](https://weibo.com/u/{data['weibo']})", inline = False)

        else:
            embed = discord.Embed(description=f"❌ {name}의 대한 정보를 찾을수 없습니다.", color=0x808080)
            return await interaction.response.send_message(embed=embed, ephemeral=True)

        await interaction.response.send_message(embed=embed)

    @app_commands.command(name = "aespa", description="aespa's SNS")
    @app_commands.choices(member=[
            app_commands.Choice(name="KARINA", value="karina"),
            app_commands.Choice(name="GISELLE", value="giselle"),
            app_commands.Choice(name="WINTER", value="winter"),
            app_commands.Choice(name="NINGNING", value="ningning")
        ])
    async def aespa(self, interaction: discord.Interaction, member:str = None):
        if member is None:
            return await self.send_sns(interaction, "aespa")

        await self.send_sns(interaction, member)

async def setup(bot) :
    await bot.add_cog(Aespa(bot))