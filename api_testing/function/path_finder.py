import os

path = os.getcwd()
while not 'data' in os.listdir(path):
    path = os.path.dirname(path)
data_path = os.path.abspath(os.path.join(path, 'data'))
