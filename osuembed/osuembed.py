import discord
import pycountry


default_embed_color = 0xffffff
default_footer_icon = 'https://raw.githubusercontent.com/ppy/osu-resources/51f2b9b37f38cd349a3dd728a78f8fffcb3a54f5/osu.Game.Resources/Textures/Menu/logo.png'


async def beatmapset(beatmapset, color=default_embed_color):
    if beatmapset:
        body = "%s\n\n" % (beatmapset.artist)

        for beatmap in beatmapset.beatmaps:
            try:
                body += "%s ☆ %s [%s] \n" % (str(round(float(beatmap.difficultyrating), 2)), beatmap.version, beatmap.gamemode)
            except:
                pass
        if len(body) > 2048:
            body = "%s" % (beatmapset.artist)
        embed = discord.Embed(
            title=beatmapset.title,
            url=beatmapset.url,
            description=body,
            color=int(color)
        )
        embed.set_author(
            name=beatmapset.creator,
            url="https://osu.ppy.sh/users/%s" % (beatmapset.creator_id),
            icon_url="https://a.ppy.sh/%s" % (beatmapset.creator_id)
        )
        embed.set_thumbnail(
            url=beatmapset.thumb
        )
        embed.set_footer(
            text=beatmapset.source,
            icon_url=default_footer_icon
        )
        return embed
    else:
        return None


async def user(user, color=default_embed_color):
    if user:
        body = ""

        if user.country:
            try:
                country = pycountry.countries.get(
                    alpha_2=user.country.upper())
                country_flag_emote = ":flag_%s:" % (
                    country.alpha_2.lower())
                body += "%s %s\n" % (country_flag_emote, country.name)
            except:
                pass

        if user.pp:
            body += "%spp (#%s)\n" % (user.pp, user.rank)

        body += "Joined osu on: %s\n" % (user.join_date)

        embed = discord.Embed(
            title=user.username,
            url=user.url,
            color=color,
            description=body,
        )
        embed.set_thumbnail(
            url=user.avatar
        )
        return embed
    else:
        return None