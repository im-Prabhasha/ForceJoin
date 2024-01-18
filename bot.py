from pyrogram import Client

# Replace 'YOUR_API_ID_1', 'YOUR_API_HASH_1', 'YOUR_BOT_TOKEN_1',
# 'YOUR_API_ID_2', 'YOUR_API_HASH_2', 'YOUR_BOT_TOKEN_2', and so on
# with the actual values.
api_ids = ['YOUR_API_ID_1', 'YOUR_API_ID_2', 'YOUR_API_ID_3', 'YOUR_API_ID_4', 'YOUR_API_ID_5',
           'YOUR_API_ID_6', 'YOUR_API_ID_7', 'YOUR_API_ID_8', 'YOUR_API_ID_9', 'YOUR_API_ID_10']

api_hashes = ['YOUR_API_HASH_1', 'YOUR_API_HASH_2', 'YOUR_API_HASH_3', 'YOUR_API_HASH_4', 'YOUR_API_HASH_5',
              'YOUR_API_HASH_6', 'YOUR_API_HASH_7', 'YOUR_API_HASH_8', 'YOUR_API_HASH_9', 'YOUR_API_HASH_10']

bot_tokens = ['YOUR_BOT_TOKEN_1', 'YOUR_BOT_TOKEN_2', 'YOUR_BOT_TOKEN_3', 'YOUR_BOT_TOKEN_4', 'YOUR_BOT_TOKEN_5',
              'YOUR_BOT_TOKEN_6', 'YOUR_BOT_TOKEN_7', 'YOUR_BOT_TOKEN_8', 'YOUR_BOT_TOKEN_9', 'YOUR_BOT_TOKEN_10']

# Replace 'your_channel_username' with your actual channel username
channel_username = '@your_channel_username'

def join_channel(api_id, api_hash, bot_token):
    app = Client(
        "bot",
        api_id=api_id,
        api_hash=api_hash,
        bot_token=bot_token
    )

    with app:
        app.join_chat(channel_username)
        print(f"Bot with token {bot_token} has joined the channel.")

def main():
    for i in range(10):
        join_channel(api_ids[i], api_hashes[i], bot_tokens[i])

if __name__ == "__main__":
    main()
