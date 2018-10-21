import json
import requests

match_id = "4176292722"
replay_json = requests.get(
                "https://api.opendota.com/api/replays?match_id=%s" % (match_id))

replay_dict = json.loads(replay_json.text)
replay_salt = replay_dict[0]["replay_salt"]
replay_cluster = replay_dict[0]["cluster"]
replay_filename = "%s_%s.dem.bz2" % (match_id, replay_salt)
download_url = "replay%s.valve.net/570/%s" % (replay_cluster, replay_filename)
#print (download_url)
r = requests.get(download_url, stream=True)
r.raw.decode_content = True # Content-Encoding