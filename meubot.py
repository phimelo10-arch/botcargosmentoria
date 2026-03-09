import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

# ==========================================
# CONFIGURAÇÕES
# ==========================================
IDS_USUARIOS_PERMITIDOS = [1445574384256417963, 666319038112202763, 1426235349457174643, 997243372207091762]
ID_CANAL_ESPECIFICO = 1480575575889412298

ID_CARGO_ALUNO_RUBIA = 1480577534709076119
ID_CARGO_ALUNO_FE = 1469085056902365397

# Puxa o Token de forma segura do Coolify / .env
TOKEN_DO_BOT = os.getenv('DISCORD_TOKEN')
# ==========================================

@bot.event
async def on_ready():
    print(f'✅ Bot online! Logado como {bot.user}')

def comando_permitido(ctx):
    return (
        ctx.channel.id == ID_CANAL_ESPECIFICO
        and ctx.author.id in IDS_USUARIOS_PERMITIDOS
    )

# =========================
# COMANDOS DE ADICIONAR
# =========================

@bot.command(name='alunorubia')
async def dar_alunorubia(ctx, membro: discord.Member = None):
    if ctx.channel.id != ID_CANAL_ESPECIFICO:
        return
    if ctx.author.id not in IDS_USUARIOS_PERMITIDOS:
        await ctx.send("❌ Você não tem permissão para usar este comando.")
        return
    if membro is None:
        await ctx.send("⚠️ Marque um usuário! Exemplo: `!alunorubia @usuario`")
        return

    cargo = ctx.guild.get_role(ID_CARGO_ALUNO_RUBIA)
    if cargo is None:
        await ctx.send("🔍 O cargo não foi encontrado no servidor. Verifique o ID.")
        return

    try:
        await membro.add_roles(cargo)
        await ctx.send(f"🎉 O cargo **{cargo.name}** foi dado para {membro.mention} com sucesso!")
    except discord.Forbidden:
        await ctx.send("🚨 Meu cargo precisa estar acima do cargo que estou tentando dar.")

@bot.command(name='alunofe')
async def dar_alunofe(ctx, membro: discord.Member = None):
    if ctx.channel.id != ID_CANAL_ESPECIFICO:
        return
    if ctx.author.id not in IDS_USUARIOS_PERMITIDOS:
        await ctx.send("❌ Você não tem permissão para usar este comando.")
        return
    if membro is None:
        await ctx.send("⚠️ Marque um usuário! Exemplo: `!alunofe @usuario`")
        return

    cargo = ctx.guild.get_role(ID_CARGO_ALUNO_FE)
    if cargo is None:
        await ctx.send("🔍 O cargo não foi encontrado no servidor. Verifique o ID.")
        return

    try:
        await membro.add_roles(cargo)
        await ctx.send(f"🎉 O cargo **{cargo.name}** foi dado para {membro.mention} com sucesso!")
    except discord.Forbidden:
        await ctx.send("🚨 Meu cargo precisa estar acima do cargo que estou tentando dar.")

# =========================
# COMANDOS DE REMOVER
# =========================

@bot.command(name='removeralunorubia')
async def remover_alunorubia(ctx, membro: discord.Member = None):
    if ctx.channel.id != ID_CANAL_ESPECIFICO:
        return
    if ctx.author.id not in IDS_USUARIOS_PERMITIDOS:
        await ctx.send("❌ Você não tem permissão para usar este comando.")
        return
    if membro is None:
        await ctx.send("⚠️ Marque um usuário! Exemplo: `!removeralunorubia @usuario`")
        return

    cargo = ctx.guild.get_role(ID_CARGO_ALUNO_RUBIA)
    if cargo is None:
        await ctx.send("🔍 O cargo não foi encontrado no servidor. Verifique o ID.")
        return

    if cargo not in membro.roles:
        await ctx.send(f"ℹ️ {membro.mention} não possui o cargo **{cargo.name}**.")
        return

    try:
        await membro.remove_roles(cargo)
        await ctx.send(f"✅ O cargo **{cargo.name}** foi removido de {membro.mention} com sucesso!")
    except discord.Forbidden:
        await ctx.send("🚨 Meu cargo precisa estar acima do cargo que estou tentando remover.")

@bot.command(name='removeralunofe')
async def remover_alunofe(ctx, membro: discord.Member = None):
    if ctx.channel.id != ID_CANAL_ESPECIFICO:
        return
    if ctx.author.id not in IDS_USUARIOS_PERMITIDOS:
        await ctx.send("❌ Você não tem permissão para usar este comando.")
        return
    if membro is None:
        await ctx.send("⚠️ Marque um usuário! Exemplo: `!removeralunofe @usuario`")
        return

    cargo = ctx.guild.get_role(ID_CARGO_ALUNO_FE)
    if cargo is None:
        await ctx.send("🔍 O cargo não foi encontrado no servidor. Verifique o ID.")
        return

    if cargo not in membro.roles:
        await ctx.send(f"ℹ️ {membro.mention} não possui o cargo **{cargo.name}**.")
        return

    try:
        await membro.remove_roles(cargo)
        await ctx.send(f"✅ O cargo **{cargo.name}** foi removido de {membro.mention} com sucesso!")
    except discord.Forbidden:
        await ctx.send("🚨 Meu cargo precisa estar acima do cargo que estou tentando remover.")

# Verificação de segurança antes de ligar o bot
if __name__ == "__main__":
    if TOKEN_DO_BOT is None:
        print("❌ ERRO FATAL: O Token do bot não foi encontrado nas Variáveis de Ambiente!")
    else:
        bot.run(TOKEN_DO_BOT)
