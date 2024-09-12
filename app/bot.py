from dotenv import load_dotenv
import os
import discord
import boto3

#load the info from the env file into the environmental variables
load_dotenv()

#AWS
dynamodb = boto3.resource (
    'dynamodb',
    region_name = os.getenv('AWS_REGION'),
    aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
)

table = dynamodb.Table(os.getenv('DYNAMODB_TABLE_NAME'))

print(f"Connected to DynamoDB table: {table.table_name}")

print("Ensuring connection...")

table.put_item(
    Item={
        'user_id': 'test_user',
        'points' : 100
    }
)

response = table.get_item(Key = {'user_id': 'test_user'})
if 'Item' in response:
    print(f"Connection ensured. Response: {response['Item']}")
    
    print("Deleting test user...")
    table.delete_item(
        Key={
            'user_id': 'test_user'
        }
    )
else:
    print("Error X-X: Test user not found. Table potentially not connected.")

#Discord
TOKEN = os.getenv('DISCORD_BOT_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    #Prevents bot from responding to itself
    if message.author == client.user:
        return
    
    #Only admins(or specified role) can manipulate points
    # admin_role = discord.utils.get(message.guild.roles, name="Support")
    # if admin_role not in message.author.roles:
    #     await message.channel.send(f"Sorry, {message.author.name}, you do not have permission to add points")
    #     return
    
    #Handle points addition command
    if message.content.startswith("!addpoints"):
        #Checking for valid use of command
        parts = message.content.split()
        if len(parts) < 2:
            await message.channel.send(f"Usage: !addpoints @user")
        return
    
        #Get mentioned user
        
    

client.run(TOKEN)
