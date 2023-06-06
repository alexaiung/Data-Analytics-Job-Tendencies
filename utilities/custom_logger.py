from datetime import datetime
import os

class CustomLogger():
    def __init__(self, log):
        self.log = log

    @staticmethod
    def info(text):
        filename = datetime.now().strftime('%Y%m%d-%H')
        #os.makedirs(f'logs/{filename}.txt')
        with open(f'logs/{filename}.txt', 'a', encoding="utf-8") as file:
            file.write(f"{datetime.now().strftime('%Y/%m/%d %H:%M:%S')} - {text}")
            file.write('\n\n')
            
