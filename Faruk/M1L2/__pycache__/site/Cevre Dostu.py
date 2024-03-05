import discord
from discord.ext import commands
from bot_mantik import gen_pass
import random
import os
print(os.listdir('resimler'))
img_name = os.listdir('resimler')




a = random.randint(1, 2)

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)



@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')


@bot.command()
async def yardım(ctx):
    await ctx.send(f'komutlar 1.çöp 2.kirlilik 3.sokak hayvanları')

@bot.command()
async def çöp(ctx):
    await ctx.send(f'Herkesi bilgilendirip insanlara yardım etmesini sağlıya bilirsin veya ilgili bir kurumla görüşüp bu durum söyleyebilirsin')
    with open('resimler\çöp.jpg', 'rb') as f:
        picture = discord.File(f)
        # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)
        
    
@bot.command()
async def kirlilik(ctx):
    await ctx.send(f'ne tür bir kirlilik bu?')

    @bot.command()
    async def hava(ctx):
        await ctx.send(f'bu durumda yakınlarda bir fabrika olabilir bu fabrikayla iletişime geçip filtre kullanmasını isteye bilirsin')
        with open('resimler\hava.jpg', 'rb') as f:
            picture = discord.File(f)
            # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
        await ctx.send(file=picture)
        await ctx.send(f'daha fazla bilgi için:')
        await ctx.send(f'https://www.youtube.com/watch?v=KdJxuQ0pof4')
        
    @bot.command()
    async def su(ctx):
        await ctx.send(f'bu durumda yakınlarda bir fabrika olabilir bu fabrikayla iletişime geçip suya atıklarını dökmemesini sağlayabilirsin')
        with open('resimler\water.png', 'rb') as f:
            picture = discord.File(f)
            # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
        await ctx.send(file=picture)
        await ctx.send(f'daha fazla bilgi için:')
        await ctx.send(f'https://www.youtube.com/watch?v=gLtyn6UyCwk')
        
    @bot.command()
    async def toprak(ctx):
        await ctx.send(f'bu durumda yakınlarda bir fabrika olabilir bu fabrikayla iletişime geçip filtre kullanmasını isteye bilirsin bu sayede bulutlarla  karbondiyoksit birleşmeyecek ve asit yağmurları olmayacak ve bu sayede kirli su toprağa karışmayacak')
        with open('resimler\indir.jpg', 'rb') as f:
            picture = discord.File(f)
            # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
        await ctx.send(file=picture)
        await ctx.send(f'daha fazla bilgi için:')
        await ctx.send(f'https://www.youtube.com/watch?v=EWAzL4Rfbqw')
    @bot.command()
    async def sokak_hayvanları(ctx):
        await ctx.send(f'eğer sokak hayvasları sorun yaşıyorsa onları sahilenebilir veya onları barınağa götürebilirsin')
        with open('resimler\petting-dog-.png', 'rb') as f:
            picture = discord.File(f)
        # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
        await ctx.send(file=picture)
        await ctx.send(f'daha fazla bilgi için:')
        await ctx.send(f'https://www.youtube.com/watch?v=pktNdiGk8yw')

bot.run("MTEzNjY5ODgwOTQ3MzMwNjcyNA.Gh8Hut.FjhOhbtv220D3X_eh9A_mnYtMJOXSIdMHrD-8c")
