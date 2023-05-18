import re
import datetime
import pandas as pd
import json
from utils import *


if __name__ == "__main__":

	# with open("output/output_20230510_2311.json", 'r') as f:
	# 	for _ in range(2):
	# 		next(f)
	# 	for line in f:
	# 		json_data = json.loads(line)
	# 		if "video_title" in json_data:
	# 			print(json_data["preroll_ad_reasons"])

	project_name = "dontcrimeme"
	bucket_name = "youtube-ads-2023"

	# upload_from_directory(project_name, bucket_name, "UserData_happysquare89/", "UserData_happysquare89/")
	upload_blob(project_name, bucket_name, "pretty_output/pretty_output_20230517_2238_combined.json", "pretty_output/pretty_output_20230517_2238_combined.json")


			





