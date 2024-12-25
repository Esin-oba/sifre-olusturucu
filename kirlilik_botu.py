import random

# discord modülünü içe aktarıyoruz
import discord
from discord.ext import commands

# Botun çalıştığını görebilmek için TOKEN kısmına kendi bot token'ınızı koymalısınız.
TOKEN = 'MTMxMzkzNTM2NTc1NjY4NjM2Ng.GF15WU.bwQK_-HbxtuHNC-JxMDkNfdE7ctfrgZNmB21l4'
intents = discord.Intents.default()
intents.message_content = True
# Botumuzun çalışacağı prefix (ön ek) belirlenir. Bu örnekte, komutlar için ön ek olarak "!" kullanıyoruz.
bot = commands.Bot(command_prefix='!',intents=intents)

# Bot çevrimiçi olduğunda çalışan olay
@bot.event
async def on_ready():
    # Botun başarılı bir şekilde çalıştığını gösteren mesaj
    print(f'{bot.user} çevrimiçi!')

# Basit bir komut ekliyoruz: Merhaba komutu
@bot.command()
async def merhaba(ctx):
    # ctx, komutun çalıştırıldığı bağlamı ifade eder
    await ctx.send(f'Merhaba {ctx.author.mention}!')  # Komutu çalıştıran kişiye "Merhaba" der.

# Toplama işlemi yapan bir komut ekleyelim
@bot.command()
async def topla(ctx, a: int, b: int):
    # Komutu çalıştıran kişiye iki sayıyı toplar ve sonucu döner
    sonuc = a + b
    await ctx.send(f'{a} + {b} = {sonuc}')
    
@bot.command()
async def sifre(ctx, uzunluk):
    elements = "+-/*!&$#?=@<>"
    password = ""

    try:
        uzunluk = int(uzunluk)
        
    except:
        await ctx.send('lütfen bir sayı giriniz!!!!')
        return

    if uzunluk > 20 or uzunluk < 0:
        await ctx.send('lütfen 0-20 arasında bir sayı giriniz!!!!')
        return

    for i in range(int(uzunluk)):
        password += random.choice(elements)
    
    await ctx.send(f'Şifreniz: {password}')

@bot.command()
async def kirlilik(ctx, uzunluk):
    atik = ["yağlı balast", "sintine", "slaç", "slop", "atık yağ", "yük artıkları", "atık su", "çöp"]
    cesit = ""

    try:
        uzunluk = int(uzunluk)

    except:
        await ctx.send('lütfen bir sayı giriniz!!!!')
        return
    
    if uzunluk >8 or uzunluk < 1:
        await ctx.send('lütfen 1-8 arasında bir sayı giriniz!!!!')
        return
    
    if uzunluk >1 or uzunluk <= 8:
        cesit += random.choice(atik)

    await ctx.send(f'cevap: {cesit}')
    


# Hata yönetimi: Hataları yakalayarak kullanıcıya daha dostça bir mesaj gösterelim
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        # Eğer eksik bir argüman varsa kullanıcıyı bilgilendirir
        await ctx.send('Bu komut için gerekli argümanları eksiksiz girin!')
    elif isinstance(error, commands.CommandNotFound):
        # Eğer geçersiz bir komut girilirse kullanıcıyı bilgilendirir
        await ctx.send('Bu geçerli bir komut değil!')



# Bot tokeni ile giriş yap
bot.run(TOKEN)
