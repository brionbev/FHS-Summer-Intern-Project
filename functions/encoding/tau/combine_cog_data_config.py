'''Environmental variables for combine cog data'''


from pathlib import Path


data_path = str(Path('.').absolute()).split('summer_data_team',maxsplit=1)[0] + 'summer_data_team\\data'



dvoice_path = data_path + '\\dvoice.json'

dr_path = data_path + '\\dementia_review.json'

np_path = data_path + '\\np.json'

                