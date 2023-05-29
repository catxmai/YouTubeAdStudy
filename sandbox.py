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
	upload_blob(project_name, bucket_name, "pretty_output/pretty_output_20230526_1750.json", "pretty_output/pretty_output_20230526_1750.json")
	# upload_blob(project_name, bucket_name, "pretty_output/pretty_output_20230518_1957.json", "pretty_output/pretty_output_20230518_1957.json")



