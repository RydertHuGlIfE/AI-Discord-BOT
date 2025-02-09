from ast import expr_context
import discord 
from discord.ext import commands
import google.generativeai as genai
from discord import app_commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

user_context = {}
bot_own = 844143559509803023
logs = []

@bot.tree.command(name="refresh", description="Refreshes the bot by clearing context and logs.")
async def refresh(interaction: discord.Interaction):
    if interaction.user.id != bot_own:
        await interaction.response.send_message("You are not allowed to access this command. Please contact the developer. Automated Request Has been logged.", ephemeral=False)
    else:
        user_context.clear()
        logs.clear()
        await interaction.response.send_message("Bot refreshed! Context and logs cleared.")


def log_denied_command_access(interaction: discord.Interaction, command_name: str):
    username = interaction.user.name
    logs.append((username, command_name))


genai.configure(api_key="AIzaSyAmdmSD8cLq7OgUUqvxIk1MwBJDwmUKGsI")
model = genai.GenerativeModel("gemini-1.5-flash")

@bot.tree.command(name="chat", description="Chat with the bot!")
async def chat(interaction: discord.Interaction, prompt: str):
    
    try:
        user_context[interaction.user.id] = [prompt]
        response = model.generate_content(prompt)
        await interaction.response.send_message(f"{response.text}")
    except Exception as e:
        await interaction.response.send_message(f"An error occured {e} Please Try again!")

@bot.tree.command(name="show_logs", description="Displays the unauthorized usage logs")
async def show_logs(interaction: discord.Interaction):
    if interaction.user.id != bot_own:
        await interaction.response.send_message(
            "You are not authorized to access this command.", ephemeral=False
        )
        log_denied_command_access(interaction, "logs")
    else:
        if not logs:
            await interaction.response.send_message("No logs to display.", ephemeral=False)
        else:
            log_messages = "\n".join([f"{user} used {command}" for user, command in logs])
            await interaction.response.send_message(f"Unauthorized Logs:\n{log_messages}", ephemeral=True)
            
@bot.tree.command(name="reply", description="Bot remembers the last chat you did!")
async def reply(interaction: discord.Interaction, prompt: str):
    if interaction.user.id in user_context:
        user_context[interaction.user.id].append(prompt)
        con_his = "\n".join(user_context[interaction.user.id])

        try:
            response = model.generate_content(con_his)
            await interaction.response.send_message(f"AI Response: {response.text}")
        except Exception as e:
            await interaction.response.send_message(f"An error occurred: {e}")
    else:
        await interaction.response.send_message("No active conversation found. Start a conversation using `/chat`.")
            
@bot.tree.command(name="ping", description="Displays The Current Ping")
async def ping(interaction: discord.Interaction):
    lat = bot.latency*1000
    rlat = round(lat, 2)
    await interaction.response.send_message(f"The Current Ping is: {rlat} ms")

@bot.tree.command(name="about", description="Tells About the Bot")
async def about(interaction: discord.Interaction):
    await interaction.response.send_message("Greetings User, This Bot is being developed by: ```__ryder__2001__```\n This Bot uses Gemini API Flash 1.5 which is tweaked a bit for discord and is currently under development")

@bot.tree.command(name="shutdown", description="Developer Commands")
async def shutdown(interaction: discord.Interaction):
    if interaction.user.id != bot_own:
        log_denied_command_access(interaction, "shutdown")
        await interaction.response.send_message("You are not allowed to access this command please contact the developer, Automated Request Has been logged.", ephemeral=False)
    else:
        await interaction.response.send_message("Shutting down bot, Code 0")
        await bot.close()

@bot.tree.command(name="show_users", description="Developer Commands")
async def users(interaction: discord.Interaction):
    if interaction.user.id != bot_own:
        log_denied_command_access(interaction, "show_users")
        await interaction.response.send_message("You are not allowed to access this command please contact the developer, Automated Request Has been logged.", ephemeral=False)
    else:
        if not user_context:
            await interaction.response.send_message("No active users found.")
        else:
            active_users = "\n".join(
                [f"<@{user_id}>: {len(context)} messages" for user_id, context in user_context.items()]
            )
            await interaction.response.send_message(f"Active Users:\n{active_users}")

@bot.tree.command(name="context_clear", description="Developer Command")
async def cclear(interaction: discord.Interaction):
    if interaction.user.id != bot_own:
        log_denied_command_access(interaction, "shutdown")
        await interaction.response.send_message("You are not allowed to access this command please contact the developer Automated Request Has been logged.", ephemeral=False)
    else:
        user_context.clear()
        await interaction.response.send_message("All Context Has been Cleared.", ephemeral=False)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    try:
        await bot.tree.sync()
        print("Slash commands synced successfully!")
    except Exception as e:
        print(f"Failed to sync slash commands: {e}")

bot.run('Add Api key here')
    
