'''Environmental variables for combine cog data'''


from pathlib import Path
import os

data_path = os.path.abspath(os.path.join("..\\functions" , "\\data"))
# data_path = str(Path('.').absolute()).split('summer_data_team',maxsplit=1)[0] + '\\data'
print(data_path)


dvoice_path = data_path + '\\dvoice.json'

dr_path = data_path + '\\dementia_review.json'

np_path = data_path + '\\np.json'

                