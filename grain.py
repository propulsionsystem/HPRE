from __init__ import *
class grain:
    def __init__(grain_data_path):
        with open(grain_data_path) as file:
            grain_params=json.load(file)

    def display_grain(self):
        