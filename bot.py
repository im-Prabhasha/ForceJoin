from pyrogram import Client

# Replace 'YOUR_API_ID_1', 'YOUR_API_HASH_1', 'YOUR_BOT_TOKEN_1',
# 'YOUR_API_ID_2', 'YOUR_API_HASH_2', 'YOUR_BOT_TOKEN_2', and so on
# with the actual values.
api_ids = ['29301453', '24365770']

api_hashes = ['aaf265964f64b744218fbebdd79c5319', '29afc2eeacd1741455d285cf48bb1c22']


# Replace 'your_channel_username' with your actual channel username
channel_username = '@sinhalastatus'

def join_channel(api_ids, api_hashs):
    app = Client(
        "bot",
        api_id=api_ids,
        api_hash=api_hashs
    )

    with app:
        app.join_chat(channel_username)
        print(f"Bot with token im has joined the channel.")

def main():
    for i in range(2):
        join_channel(api_ids[i], api_hashes[i])

if __name__ == "__main__":
    main()
