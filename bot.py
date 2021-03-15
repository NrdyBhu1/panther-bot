from config import token, prefix
from discord import Client, Status, Streaming, File, Embed
import datetime
import random
import json
import requests
from memer import heck, get_some_joke, rip, get_random_site


class Bot(Client):
    async def on_ready(self):
        await self.change_presence(afk=True, status=Status.do_not_disturb)
        print('Logged on as', self.user)


    def get_embed(self, title, desc, color=0x000000):
        return Embed(title=title, description=desc, color=color)


    def get_help(self, args):
        help = Embed(title='Command list')
        if len(args) == 0:
            help.add_field(name=":smile: **Fun**", value="`p!commands fun`")
            help.add_field(name=":camera: **Image**", value="`p!commands img`", inline=True)
            help.add_field(name=":information_source: **Info**", value="`p!info`")
            help.add_field(name=":regional_indicator_h: **Commands**", value="`p!commands`", inline=True)
        else:
            if args[0] == 'fun':
                help.add_field(name="User Avatar", value="`p!avatar` or `p!avatar <@someone>`") 
                help.add_field(name="Search - DuckDuckGo", value="`p!duckduckgo <some words to search>`") 
                help.add_field(name="Search - Google", value="`p!google <some words to search>`") 
                help.add_field(name="Search - Wikipedia", value="`p!wikipedia <some words to search>` or `p!wiki <some words to search>`") 
                help.add_field(name="Jokes", value="`p!joke`") 
                help.add_field(name="Use Less Web", value="`p!uselessweb` or `p!uweb`") 
            elif args[0] == 'img':
                help.add_field(name="Hacker Meme", value="`p!hecker` or `p!hecker <@someone>`") 
                help.add_field(name="Rip Meme", value="`p!rip` or `p!rip <@someone>`") 
            else:
                help = self.get_embed(title="**Error**", desc="That command does not exist!! \n please try `p!commands` for commands", color=0xff0000)
        return help


    def get_string_from_arr(self, arr):
        final_str = ""
        for i in range(len(arr)):
            if i != 0:
                final_str += "+" + str(arr[i])
            else:
                final_str += str(arr[i])
        return final_str


    async def on_message(self, msg):
        # don't respond to ourselves
        if msg.author == self.user:
            return

        if msg.content.startswith(prefix):
            
            # send_website = random.randint(0, 50) > 20

            # if send_website:
                # await msg.channel.send("You can also take a look at my website at \n https://pantherbot.netlify.app/ \n :wink:")

            content = msg.content.replace(prefix, "")
            command = content.split(" ")[0]
            args = content.split(" ")
            args.pop(0)

            if command == 'ping':
                await msg.channel.send(f'**PONG** \n 🏓**Latency** is {datetime.datetime.now()  - msg.created_at}ms')

            elif command == 'google':
                if len(args) > 0:
                    await msg.channel.send(f'https://google.com/search?q={self.get_string_from_arr(args)}')
                else:
                    await msg.channel.send(":angry: Give search parameters")

            elif command == 'duckduckgo':
                if len(args) > 0:
                    await msg.channel.send(f'https://duckduckgo.com/?q={self.get_string_from_arr(args)}')
                else:
                    await msg.channel.send(":angry: Give search parameters")
            
            elif command == 'yahoo':
                if len(args) > 0:
                    await msg.channel.send('ughhhh \n what even \n who even uses yahoo these days')
                else:
                    await msg.channel.send(":angry: Give search parameters")
    
            elif command == 'wiki' or command == 'wikipedia':
                if len(args) > 0:
                    await msg.channel.send(f'https://en.wikipedia.org/wiki/{self.get_string_from_arr(args)}')
                else:
                    await msg.channel.send(":angry: Give search parameters")

            elif command == 'help':
                await msg.reply("No help provided :laughing: ")

            elif command == 'hecker':
                if len(args) == 0:
                    heck(msg.author.avatar_url).save(f"customs/hecker_{msg.author}.png")
                    await msg.channel.send(file=File(f"./customs/hecker_{msg.author}.png"))
                else:
                    heck(msg.mentions[0].avatar_url).save(f"customs/hecker_{msg.mentions[0]}.png")
                    await msg.channel.send(file=File(f"./customs/hecker_{msg.mentions[0]}.png"))

            elif command == 'rip':
                if len(args) == 0:
                    rip(msg.author.avatar_url).save(f"customs/rip_{msg.author}.png")
                    await msg.channel.send(file=File(f"./customs/rip_{msg.author}.png"))
                else:
                    rip(msg.mentions[0].avatar_url).save(f"customs/rip_{msg.mentions[0]}.png")
                    await msg.channel.send(file=File(f"./customs/rip_{msg.mentions[0]}.png"))

            elif command == 'joke':
                await msg.channel.send(get_some_joke())

            elif command == 'commands':
                await msg.channel.send(embed=self.get_help(args))

            elif command == 'avatar':
                if len(args) == 0:
                    await msg.channel.send(msg.author.avatar_url)
                else:
                    await msg.channel.send(msg.mentions[0].avatar_url)

            elif command == 'info':
                await msg.channel.send(embed=self.get_embed(title="**Info**", desc='A bot Made By [NrdyBhu1](https://nrdybhu1.github.io) \n Written in python[idk why] \n\n Click [here](https://discord.com/oauth2/authorize?client_id=778215416623398935&scope=bot&permissions=0) to invite me \n\n Join the [discord server](https://discord.gg/8SsNe3Ax68) for more fun.'))

            elif command == 'invite':
                await msg.channel.send(embed=self.get_embed(title="**Invite**", desc="Click [here](https://discord.com/oauth2/authorize?client_id=778215416623398935&scope=bot&permissions=0) to invite me \n\n Join the [discord server](https://discord.gg/8SsNe3Ax68) for more fun."))
            
            elif command == 'uselessweb' or command == 'uweb':
                await msg.channel.send(get_random_site())

            elif command == 'oof':
                await msg.reply('https://tenor.com/view/off-size-off-wacky-face-pouty-lips-gif-16675463')

            else:
                await msg.channel.send(embed=self.get_embed(title="**Error**", desc="That command does not exist!! \n please try `p!commands` for commands", color=0xff0000))

        elif msg.content == 'ping':
            await msg.reply('pong')

        elif msg.content.upper() == 'F':
            await msg.reply('F')

        elif msg.content == 'rip' or msg.content.count('rip') != 0:
            await msg.reply('https://tenor.com/view/rip-coffin-black-ghana-celebrating-gif-16743302')


client = Bot()
client.run(token)
