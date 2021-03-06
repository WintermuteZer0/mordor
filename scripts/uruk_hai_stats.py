# Mordor script: uruk_hai_stats.py
# Mordor script description: Provides basic stats by event log and task category
# Author: Roberto Rodriguez (@Cyb3rWard0g)
# License: GPL-3.0

import argparse
import pandas as pd
from tabulate import tabulate

# Bannner
print(r"""
 _   _            _         _   _       _   ____  _        _       
| | | |_ __ _   _| | __    | | | | __ _(_) / ___|| |_ __ _| |_ ___ 
| | | | '__| | | | |/ /____| |_| |/ _` | | \___ \| __/ _` | __/ __|
| |_| | |  | |_| |   <_____|  _  | (_| | |  ___) | || (_| | |_\__ \
 \___/|_|   \__,_|_|\_\    |_| |_|\__,_|_| |____/ \__\__,_|\__|___/ V0.1

 Creator: Roberto Rodriguez @Cyb3rWard0g
 License: GPL-3.0

 """)

# Initial description
text = 'This script allows you to get a basic count by evet log and task category'

# Initiate the parser
parser = argparse.ArgumentParser(description=text)

# Add arguments (store_true means no argument needed)
parser.add_argument("-v", "--version", help="shows version of script", action="store_true")
parser.add_argument("-f", "--file", help="file to get info from", type=str , required=True)

args = parser.parse_args()

if args.version:
    print("script version 0.1")

mordor_file = pd.read_json(args.file,lines=True)
mordor_summary = mordor_file.groupby(['log_name','task']).count()['record_number']
mordor_summary_df = mordor_summary.to_frame().sort_values(by=['log_name','record_number'],ascending=False)
mordor_summary_df_table = mordor_summary_df.reset_index(level=['task'])
print(tabulate(mordor_summary_df_table, tablefmt="github", headers="keys"))