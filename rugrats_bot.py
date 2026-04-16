import random

class RugratsBot:
    def __init__(self):
        self.emotes = {
            "rare": ["💎", "🌟", "✨"],
            "legendary": ["🦄", "🎉", "🐉"],
        }

    def on_player_join(self, player_name):
        print(f"Welcome {player_name}! Get ready for an adventure!")
        self.greet_player(player_name)

    def greet_player(self, player_name):
        print(f"Hello, {player_name}! You're awesome! 🎊")

    def kick_player(self, player_name):
        print(f"{player_name} has been kicked from the game.")

    def loop_emotes(self):
        for rarity, emotes in self.emotes.items():
            for emote in emotes:
                print(f"{rarity.capitalize()} emote: {emote}")

    def teleport_player(self, player_name, location):
        print(f"{player_name} has been teleported to {location}!")

    def betting_game(self, player_name, amount):
        winning_number = random.randint(1, 100)
        if amount > 0:
            print(f"{player_name} bet {amount}. Winning number is {winning_number}.")
            # Betting logic can be added here

    def cute_response(self):
        responses = [
            "You're purr-fect! 🐾",
            "I think you're pawsome! 😊",
            "You're a great friend! 💖"
        ]
        print(random.choice(responses))

# Example usage
bot = RugratsBot()
bot.on_player_join("Player1")
bot.loop_emotes()
bot.teleport_player("Player1", "Wonderland")
bot.betting_game("Player1", 10)
bot.cute_response()