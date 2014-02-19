# from pymongo import Connection
# import csv
# import tabular as tb
# import json

# db = Connection().cric

# def safe(line):
#     '''Strips out all unsafe / non-ASCII characters'''
#     return ''.join(char for char in line if 32 <= ord(char) < 128)

# cric_file = tb.tabarray(SVfile='first.csv',verbosity=0,headerlines=1)

# for all_data in cric_file[['India 1st Innings', 'Runs', 'Balls', '4s', '6s', 'SR']]:
#     all_data = list(all_data)
#     name,runs,balls,fours,six,strike_rate = all_data[0], all_data[1], safe(all_data[2]), all_data[3], all_data[4], all_data[5]
#     db.allmagas.insert({'name':name,
#                     'runs':runs,
#                     'balls':balls,
#                      'fours': fours ,
#                      'six': six,
#                      'strike_rate': strike_rate})

from pymongo import Connection
import pandas as pd

db = Connection().gramener

cric_file = pd.read_csv('first.csv')

data = pd.DataFrame(cric_file)

db.gramener.insert({'name': list(data['India 1st Innings'].apply(str)),
                   'Runs': list(data['Runs'].apply(str)),
                   'Balls': list(data['Balls'].apply(str)),
                   '4s': list(data['4s'].apply(str)),
                   '6s': list(data['6s'].apply(str)),
                   'SR': list(data['SR'].apply(str)) })

# db.cric.insert(cric_file.to_dict())