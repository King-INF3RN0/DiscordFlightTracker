import discord

class DiscordPoster:
    def __init__(self, client, config):
        self.client = client
        self.config = config
        self.main_channel_id = int(config["discord"]["main_channel_id"])
        self.debug_channel_id = int(config["discord"]["debug_channel_id"])
        self.mention_user_id = int(config["discord"]["mention_user_id"])

    async def post_to_main(self, message, mention_role_id=None):
        channel = self.client.get_channel(self.main_channel_id)
        if channel:
            mention = f"<@&{mention_role_id}>" if mention_role_id else ""
            await channel.send(f"{mention}\n{message}")
        else:
            print("[ERROR] Could not find main channel.")

    async def post_debug(self, message, mention_user=False):
        channel = self.client.get_channel(self.debug_channel_id)
        if channel:
            mention = f"<@{self.mention_user_id}>" if mention_user else ""
            await channel.send(f"{mention}\n{message}")
        else:
            print("[ERROR] Could not find debug channel.")
