import urllib
import json
import requests
import discord
from discord.ext import commands
import datetime
import io
import time
 
from urllib import parse, request
from PIL import Image, ImageDraw, ImageFont, ImageFile

bot = commands.Bot(command_prefix='!', description="ayuda bot") #Comando
bot.remove_command("help") # Borra el comando por defecto !help

@bot.command()
async def infoplaca(ctx, *, placa):
    await ctx.message.delete()
    await ctx.send("Generando información placa...", delete_after=0)
    time.sleep(3)
    
    response = requests.get(f"https://www.habbotravel.com/getBadgeInfo.php?badge="+placa+ "&hotel=es") 
    #habbo =  response.json()['code']
    try:

     nombre = response.json()['name']
    except KeyError:
        nombre="Aun no tiene Nombre"

    ####
    try:

     descripcion = response.json()['desc']
    except KeyError:
        descripcion="Aun no tiene descripción"
    
    url="https://images.habbo.com/c_images/album1584/"+placa+ ".png"

  
    
    
    img1 = Image.open(io.BytesIO(requests.get(url).content)).convert("RGBA")
    img1 = img1.resize((90,90), Image.Resampling.LANCZOS)
    img2 = img1.copy()

   
    
    
    
    
        
        
        
    
        
        
       
        
        

    img1 = Image.open(r"imagenes/habbobanner.png") 
    
        
        
       



    
    img1.paste(img2,(75,40), mask = img2)


    draw = ImageDraw.Draw(img1)
    font = ImageFont.truetype("fuentes/comicSans.ttf", 25) #Tamaño de la fuente (textos)

    draw.text((200, 35), f"{nombre}", font=font, fill="#fff")  #Texto y color
    ##
    draw = ImageDraw.Draw(img1)
    font = ImageFont.truetype("fuentes/comicSans.ttf", 25) #Tamaño de la fuente (textos)

    draw.text((200, 100), f"{descripcion}".replace("None","no tiene descripcion"), font=font, fill="#fff")  #Texto y color
    
   
       


      
    
       
      

      
    
       
            
        
        
        
       
        
    with io.BytesIO() as image_binary:
        img1.save(image_binary, 'PNG')
        image_binary.seek(0)

        await ctx.send(file=discord.File(fp=image_binary, filename='infoplaca.png'))
         
        
        
        
        


@bot.event
async def on_ready():
    print("BOT listo!")
    
 
    
bot.run('') #OBTEN UN TOKEN EN: https://discord.com/developers/applications    
