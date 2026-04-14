import discord
from discord.ext import commands
from discord.ui import Button, View
from flask import Flask
import threading
import os

# --- CHIÊU NGỤY TRANG CHẠY FREE 24/7 ---
app = Flask(__name__)
@app.route('/')
def home():
    return "SHADOW CARTEL BOT IS ONLINE"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

# --- CONFIG CỦA ĐẠI CA ---
TOKEN = 'MTQ5MzU5MjA1NTI3OTI1NTYxMg.GGjw7l.K3wv3UZrLQbZ4IgURJe40o143_xQWZ7QFCzXJ0'
LINK_MOI = 'https://discord.gg/w6eyJRfa'

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    activity = discord.Game(name="GTA5VN - 🅲🅷🅸🅴🅼 🅳🅾🅽🅶", type=3)
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print(f'--- [SYSTEM_BYPASS] ---')
    print(f'Bot {bot.user.name} da vao tran!')

@bot.command()
async def diemdanh(ctx):
    # KHÔI PHỤC BẢNG EMBED
    embed = discord.Embed(
        title="⊱ ⚔️ SHADOW CARTEL - CHIẾM ĐÓNG ⚔️ ⊰",
        description="**Chiếm Đóng Tổng**",
        color=0x2f3136
    )
    embed.add_field(name="📌 Cách Vào:", value="🔥 Bật hoạt động game **GTA5VN**.", inline=False)
    embed.add_field(name="📍 TRẠNG THÁI:", value="🟢 Đang Hoạt Động", inline=False)
    
    # KHÔI PHỤC NÚT BẤM "VÀO ROOM"
    view = View()
    button = Button(
        label="VÀO ROOM CHIẾM ĐÓNG", 
        style=discord.ButtonStyle.link, 
        url=LINK_MOI,
        emoji="⚔️"
    )
    view.add_item(button)
    
    await ctx.send(embed=embed, view=view)

if __name__ == "__main__":
    # Kích hoạt ngụy trang để Render không thu phí
    threading.Thread(target=run_web).start()
    # Chạy bot chính của Đại ca
    bot.run(TOKEN)
