import discord
from discord.ext import commands
from typing import cast
import wavelink
import subprocess


class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.last_member = None
        try:
            subprocess.run(["Java", "-jar", "Lavalink.Jar"], shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(e)

    @commands.Cog.listener()
    async def on_wavelink_node_ready(self, payload: wavelink.NodeReadyEventPayload) -> None:
        print(f"Wavelink node {payload.node!r} is ready")


    @commands.command()
    async def play(self, ctx: commands.Context, *, query: str) -> None:
        if not ctx.guild:
            return

        player: wavelink.Player
        player = cast(wavelink.Player, ctx.voice_client)

        if not player:
            try:
                player = await ctx.author.voice.channel.connect(cls=wavelink.Player)
            except AttributeError:
                await ctx.sent("You are not in a voice channel")
                return
            except discord.errors.ClientException:
                await ctx.send("I was unable to join this voice channel")
                return

        player.autoplay = wavelink.AutoPlayMode.enabled

        if not hasattr(player, "home"):
            player.home = ctx.channel
        elif player.home != ctx.channel:
            await ctx.send("I am already playing music in another channel")
            return

        tracks: wavelink.Search = await wavelink.Playable.search(query)
        if not tracks:
            await ctx.send("No tracks found")
            return

        if isinstance(tracks, wavelink.Playlist):
            added: int = await player.queue.put_wait(tracks)
            await ctx.send(f"Added {added} tracks to the queue")
        else:
            track: wavelink.Playable = tracks[0]
            await player.queue.put_wait(tracks)
            await ctx.send(f"Added {track.title} to the queue")

        if not player.playing:
            await player.play(player.queue.get(), volume=30)

async def setup(bot):
    await bot.add_cog(Music(bot))