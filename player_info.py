from nba_api.stats.endpoints import commonplayerinfo
from nba_api.stats.static import players
import argparse
import sys


def find_player(name):
	player_search = players.find_players_by_full_name(name)
	if len(player_search) == 0:
		print("No player with name '%s' found." % name)
		sys.exit(0) 
	player_id = player_search[0]['id']
	full_name = player_search[0]['full_name']
	player_info = commonplayerinfo.CommonPlayerInfo(player_id=player_id).get_normalized_dict()
	school = player_info['CommonPlayerInfo'][0]['SCHOOL']
	print("Player with name '%s' found! Here is some information about him:" % name)
	print("\tFull Name: %s" % full_name)
	print("\tSchool: %s" % school)

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
