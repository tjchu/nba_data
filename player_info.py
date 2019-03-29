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
	print("Found player%s matching the name '%s'" % (plural, name)) 
	for player in player_search:
		player_id = player['id']
		player_info = commonplayerinfo.CommonPlayerInfo(player_id=player_id).get_normalized_dict()

		# Player Information
		full_name = player['full_name']
		school = player_info['CommonPlayerInfo'][0]['SCHOOL']
		if '-' in player_info['CommonPlayerInfo'][0]['HEIGHT']:
			height = player_info['CommonPlayerInfo'][0]['HEIGHT'].split('-')
			height = "%s'%s''" % (height[0], height[1])
		else: 
			height = "N/A"

		print("----")
		print("Player with name '%s' found! Here is some information about him:" % name)
		print("\tFull Name: %s" % full_name)
		print("\tSchool: %s" % school)
		print("\tHeight: %s" % height)
		print("----")

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
