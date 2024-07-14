import discord
from redbot.core import commands
import aiohttp
import json
import datetime

class Earthquake(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.stop_messages = False

    @commands.command(name='earthquake', help='Get the latest earthquake information')
    async def earthquake(self, ctx, *, search_query: str = None):
        url = 'https://earthquake.usgs.gov/fdsnws/event/1/query'
        params = {
            'format': 'geojson',
            'orderby': 'time'
        }
        if search_query:
            params['query'] = search_query
        else:
            params['starttime'] = (datetime.datetime.now() - datetime.timedelta(days=7)).strftime('%Y-%m-%d')
            params['endtime'] = datetime.datetime.now().strftime('%Y-%m-%d')
            params['minmagnitude'] = '5'
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as response:
                data = await response.json()
        if response.status == 200:
            if data['metadata']['count'] > 0:
                try:
                    webhook = await ctx.channel.create_webhook(name="Earthquake Alert Webhook", avatar=self.bot.user.avatar.url)
                    for feature in data['features']:  # Send all earthquakes
                        if self.stop_messages:
                            break
                        utc_time = datetime.datetime.utcfromtimestamp(feature['properties']['time'] / 1000)
                        embed = discord.Embed(title=f"Earthquake Alert", description=f"Location: {feature['properties']['place']}", color=0x00ff00, timestamp=utc_time)
                        embed.add_field(name="Magnitude", value=feature['properties']['mag'], inline=False)
                        embed.add_field(name="Time", value=discord.utils.format_dt(utc_time, style='F'), inline=False)
                        embed.add_field(name="Depth", value=feature['geometry']['coordinates'][2], inline=False)
                        embed.add_field(name="More Info", value=f"[USGS Info Page]({feature['properties']['url']})", inline=False)
                        await webhook.send(embed=embed)
                    await webhook.delete()
                except discord.Forbidden:
                    for feature in data['features']:  # Send all earthquakes
                        if self.stop_messages:
                            break
                        utc_time = datetime.datetime.utcfromtimestamp(feature['properties']['time'] / 1000)
                        embed = discord.Embed(title=f"Earthquake Alert", description=f"Location: {feature['properties']['place']}", color=0x00ff00, timestamp=utc_time)
                        embed.add_field(name="Magnitude", value=feature['properties']['mag'], inline=False)
                        embed.add_field(name="Time", value=discord.utils.format_dt(utc_time, style='F'), inline=False)
                        embed.add_field(name="Depth", value=feature['geometry']['coordinates'][2], inline=False)
                        embed.add_field(name="More Info", value=f"[USGS Info Page]({feature['properties']['url']})", inline=False)
                        await ctx.send(embed=embed)
            else:
                await ctx.send("No earthquakes found in the given time period or matching the search query.")
        else:
            await ctx.send("Failed to fetch earthquake data.")

    @commands.command(name='eqstop', help='Stop the earthquake messages')
    async def stop_messages(self, ctx):
        self.stop_messages = True
        await ctx.send("Earthquake messages stopped.")
