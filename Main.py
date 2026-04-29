from Core.Player import Player
from Core.SaveSystem import save_player, load_player
from Core.XMLLoader import load_npc_from_xml


def main():
    print("=================================")
    print("        SOULCRAFTER")
    print("     Forge Your Fantasy")
    print("=================================")

    player = load_player()

    if player is None:
        player = Player(name="Dev")
        save_player(player)

    npc = load_npc_from_xml("Data/NPC/Frostara.xml")

    print("\nPLAYER:")
    print(player.to_dict())

    print("\nLOADED NPC:")
    print(npc.to_dict())


if __name__ == "__main__":
    main()
