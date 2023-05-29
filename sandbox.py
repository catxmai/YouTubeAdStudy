import re
import datetime
import pandas as pd
import json
import csv
from utils import *


if __name__ == "__main__":

	project_name = "dontcrimeme"
	bucket_name = "youtube-ads-2023"

	# upload_from_directory(project_name, bucket_name, "interests/", "interests/")
	# upload_blob(project_name, bucket_name, "pretty_output/pretty_output_20230526_1750.json", "pretty_output/pretty_output_20230526_1750.json")
	# upload_blob(project_name, bucket_name, "pretty_output/pretty_output_20230518_1957.json", "pretty_output/pretty_output_20230518_1957.json")

	config_path = "config.json"
	driver = create_driver(config_path, headless=True) 
	interests = collect_interests(driver)
	brands = collect_brands(driver)

	print("Topics:")
	print()
	for i in interests:
		print(i)

	print("Brands:")
	print()
	for i in brands:
		print(i)