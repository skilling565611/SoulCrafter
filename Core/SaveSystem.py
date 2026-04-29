import json
import os
from Core.Player import Player


SAVE_PATH = "Data/Saves/player_save.json"


def save_player(player):
    os.makedirs(os.path.dirname(SAVE_PATH), exist_ok=True)

    with open(SAVE_PATH, "w", encoding="utf-8") as file:
        json.dump(player.to_dict(), file, indent=4)


def load_player():
    if not os.path.exists(SAVE_PATH):
        return None

    with open(SAVE_PATH, "r", encoding="utf-8") as file:
        data = json.load(file)

    return Player.from_dict(data)
