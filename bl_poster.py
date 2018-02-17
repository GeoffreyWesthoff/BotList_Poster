import aiohttp
import requests

# class bfd_async():
#     client = aiohttp.ClientSession()
#     async def get_bot(self,id):
#         async with client.get('https://botsfordiscord.com/api/v1/bots/' + str(id)) as r:
#             return await r.json()

class NoBotListFound(Exception):
    def __init__(self):
        print('No Authorization key has been found for any supported botlist.')

class client():
    def post_bfd(bot_id, token, guild_count):
        r = requests.post('https://botsfordiscord.com/api/v1/bots/' + str(bot_id),headers={'Authorization': token}, data={'count': int(guild_count)})
        if r.status_code == 200:
            print('Succesfully posted to BotsForDiscord.com')
        else:
            print('[' + str(r.status_code) + ']: Could not post to botsfordiscord.com')

    def post_dbl(bot_id, token, guild_count, shard_id=None, shard_count=None):
        if shard_id or shard_count is not None:
            r = requests.post('https://discordbots.org/api/bots/' + str(bot_id) + '/stats', headers={'Authorization': token},
                              data={'server_count': int(guild_count), 'shard_id': int(shard_id), 'shard_count': shard_count})
        else:
            r = requests.post('https://discordbots.org/api/bots/' + str(bot_id) + '/stats',
                              headers={'Authorization': token},
                              data={'server_count': int(guild_count)})
        if r.status_code == 200:
            print('[200]: Succesfully posted to DiscordBots.org')
        else:
            print('[' + str(r.status_code) + ']: Could not post to discordbots.org')

    def post_botlistspace(bot_id, token, guild_count):
        r = requests.post('https://botlist.space/api/bots/' + str(bot_id),headers={'Authorization': token}, data={'server_count': int(guild_count)})
        if r.status_code == 200:
            print('[200]: Succesfully posted to botlist.space')
        else:
            print('['+str(r.status_code)+']: Could not post to botlist.space')

    def post_terminal(bot_id, token, guild_count):
        r = requests.post('https://ls.terminal.ink/api/v1/bots/' + str(bot_id),headers={'Authorization': token}, data={'server_count': int(guild_count)})
        if r.status_code == 200:
            print('[200]: Succesfully posted to ls.terminal.ink')
        else:
            print('[' + str(r.status_code) + ']: Could not post to ls.terminal.ink')

    def post_discordpw(bot_id, token, guild_count, shard_id=None, shard_count=None):
        if shard_id or shard_count is not None:
            r = requests.post('https://bots.discord.pw/api/bots/' + str(bot_id) + '/stats', headers={'Authorization': token},
                          data={'server_count': int(guild_count),'shard_id': shard_id, 'shard_count': shard_id})
        else:
            r = requests.post('https://bots.discord.pw/api/bots/' + str(bot_id) + '/stats', headers={'Authorization': token},
                              data={'server_count': int(guild_count),})
        if r.status_code == 200:
            print('[200]: Succesfully posted to bots.discord.pw')
        else:
            print('[' + str(r.status_code) + ']: Could not post to bots.discord.pw')

    def post_discordservices(bot_id, token, guild_count):
        r = requests.post('https://discord.services/api/bots/' + str(bot_id) + '/stats', headers={'Authorization': token},
                              data={'server_count': int(guild_count),})
        if r.status_code == 200:
            print('[200]: Succesfully posted to discord.services')
        else:
            print('[' + str(r.status_code) + ']: Could not post to discord.services')

    def post_all(bot_id, guild_count, shard_count=None, shard_id=None, dbl_token=None, botspw_token=None, botlistspace_token=None, terminal_token=None, bfd_token=None, discordservices_token=None):
        if dbl_token is None and botspw_token is None and botlistspace_token is None and terminal_token is None and bfd_token is None and discordservices_token is None:
            raise NoBotListFound()
        if dbl_token is not None:
            if shard_id or shard_count is not None:
                r = requests.post('https://discordbots.org/api/bots/' + str(bot_id) + '/stats',
                                  headers={'Authorization': dbl_token},
                                  data={'server_count': int(guild_count), 'shard_id': int(shard_id),
                                        'shard_count': shard_count})
            else:
                r = requests.post('https://discordbots.org/api/bots/' + str(bot_id) + '/stats',
                                  headers={'Authorization': dbl_token},
                                  data={'server_count': int(guild_count)})
            if r.status_code == 200:
                print('[200]: Succesfully posted to DiscordBots.org')
            else:
                print('[' + str(r.status_code) + ']: Could not post to discordbots.org')
        if botspw_token is not None:
            if shard_id or shard_count is not None:
                r = requests.post('https://bots.discord.pw/api/bots/' + str(bot_id) + '/stats',
                                  headers={'Authorization': botspw_token},
                                  data={'server_count': int(guild_count), 'shard_id': shard_id,
                                        'shard_count': shard_id})
            else:
                r = requests.post('https://bots.discord.pw/api/bots/' + str(bot_id) + '/stats',
                                  headers={'Authorization': botspw_token},
                                  data={'server_count': int(guild_count), })
            if r.status_code == 200:
                print('[200]: Succesfully posted to bots.discord.pw')
            else:
                print('[' + str(r.status_code) + ']: Could not post to bots.discord.pw')
        if botlistspace_token is not None:
            r = requests.post('https://botlist.space/api/bots/' + str(bot_id), headers={'Authorization': botlistspace_token},
                              data={'server_count': int(guild_count)})
            if r.status_code == 200:
                print('[200]: Succesfully posted to botlist.space')
            else:
                print('[' + str(r.status_code) + ']: Could not post to botlist.space')
        if terminal_token is not None:
            r = requests.post('https://ls.terminal.ink/api/v1/bots/' + str(bot_id), headers={'Authorization': terminal_token},
                              data={'server_count': int(guild_count)})
            if r.status_code == 200:
                print('[200]: Succesfully posted to ls.terminal.ink')
            else:
                print('[' + str(r.status_code) + ']: Could not post to ls.terminal.ink')
        if bfd_token is not None:
            r = requests.post('https://botsfordiscord.com/api/v1/bots/' + str(bot_id), headers={'Authorization': bfd_token},
                              data={'count': int(guild_count)})
            if r.status_code == 200:
                print('Succesfully posted to BotsForDiscord.com')
            else:
                print('[' + str(r.status_code) + ']: Could not post to botsfordiscord.com')
        if discordservices_token is not None:
            r = requests.post('https://discord.services/api/bots/' + str(bot_id) + '/stats',
                              headers={'Authorization': discordservices_token},
                              data={'server_count': int(guild_count), })
            if r.status_code == 200:
                print('[200]: Succesfully posted to discord.services')
            else:
                print('[' + str(r.status_code) + ']: Could not post to discord.services')