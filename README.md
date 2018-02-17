# BotList_Poster

## A library that helps you post to all known bot lists.

### Available functions

`post_bfd(bot_id, token, guild_count)`
Posts to botsfordiscord.com
`post_dbl(bot_id, token, guild_count, shard_id, shard_count)`
Posts to discordbots.org. shard_id and shard_count are optional
`post_botlistspace(bot_id, token, guild_count)`
Posts to botlist.space
`post_discordpw(bot_id, token, guild_count, shard_id, shard_count)`
Posts to bots.discord.pw. shard_id and shard_count are optional
`post_terminal(bot_id, token, guild_count)`
Posts to ls.terminal.ink.
`post_discordservices(bot_id, token, guild_count)`
Posts to discord.services.
`post_all(bot_id, guild_count, shard_count, shard_id, dbl_token, botspw_token, botlistspace_token, terminal_token, bfd_token, discordservices_token)`
Posts to all of the above botlists. Only 1 token has to be included at least. shard_count and shard_id are optional.

### Example code

```python
import discord
import bl_poster

client = discord.Client()

@client.even
async def on_ready():
    guild_count = len(client.guilds)
    bot_id = client.user.id
    dbl_token = "DFJKLDHKJLDSFHDFKLJFHSLKJSDF" #Should get this on bot list site
    bl_poster.client.post_all(bot_id, guild_count, dbl_token=dbl_token)

client.run("actual_bot_token")
```
