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

	# upload_from_directory(project_name, bucket_name, "interests/", "interests/")
	upload_blob(project_name, bucket_name, "pretty_output/pretty_output_20230526_1750.json", "pretty_output/pretty_output_20230526_1750.json")
	# upload_blob(project_name, bucket_name, "pretty_output/pretty_output_20230518_1957.json", "pretty_output/pretty_output_20230518_1957.json")


			





