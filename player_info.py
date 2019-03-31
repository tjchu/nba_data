from nba_api.stats.endpoints import commonplayerinfo
from nba_api.stats.static import players
import argparse
import sys


def find_player(name):
	player_search = players.find_players_by_full_name(name)
	plural = ""
	if len(player_search) == 0:
		print("No player with name '%s' found." % name)
		sys.exit(0)
	if len(player_search) > 1:
		plural = "s"
	print("Found player%s matching the name '%s'!" % (plural, name)) 
	for player in player_search:
		player_id = player['id']
		player_info = commonplayerinfo.CommonPlayerInfo(player_id=player_id).get_normalized_dict()

		# Display the players' information
		print("----")
		for info_key, info_value in player_info['CommonPlayerInfo'][0].items():
			print(info_key + ": " + str(info_value))

	return

"""
lebron_info = commonplayerinfo.CommonPlayerInfo(player_id=2544)
print(lebron_info.get_normalized_dict())
print(lebron_info.get_normalized_dict()['CommonPlayerInfo'])
"""

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-n", "--name", help="Player Full Name", type=str)
	args = parser.parse_args()

	find_player(args.name)
	sys.exit(0)
