from nba_api.stats.endpoints import commonplayerinfo
from nba_api.stats.static import players
import argparse
from util import info, err
import sys

# Output NBA player headline info
def find_player(player_name):
	return

def player_average_stats(player_name):
	player_search = players.find_players_by_full_name(player_name)
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
		#print("----General Information----")
		#for info_key, info_value in player_info['CommonPlayerInfo'][0].items():
		#	print(info_key + ": " + str(info_value))
		for stats_key, stats_value in player_info["PlayerHeadlineStats"][0].items():
			if stats_key in ["PLAYER_ID", "PLAYER_NAME"]:
				continue
			print(stats_key + ": " + str(stats_value))

def player_exists(name):
	search_result = find_players_by_full_name(name)
	if not search_result: 
		err("Player '%s' doesn't exist." % name)	
	info(search_result)

"""
lebron_info = commonplayerinfo.CommonPlayerInfo(player_id=2544)
print(lebron_info.get_normalized_dict())
print(lebron_info.get_normalized_dict()['CommonPlayerInfo'])
"""

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-n", "--name", help="Player Full Name", type=str)
	parser.add_argument("-d", "--date", help="Date of the game played, defaults to latest game if not entered", type=str)
	args = parser.parse_args()
	info("NBA Player Analysis program started.")
	player_name = None
	if not args.name:
		while not player_name: 
			player_name = input("Please input NBA player name: ")
	else:
		player_name = args.name
	find_player(player_name)
	sys.exit(0)
