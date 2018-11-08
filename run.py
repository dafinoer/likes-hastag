import json
import os
import re
from datetime import datetime
import pendulum

from wordcloud import WordCloud


import numpy 
import pandas
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from dateutil.relativedelta import relativedelta


path = os.path.dirname(os.path.abspath(__file__))

name_file = "profiles/dafinrs_2018-11-05 14-21-57.json"


def main():

    name_dir = '{}/profiles/'.format(path)

    path_json = 'profiles/'

    json_files = [pas_json for pas_json in os.listdir(name_dir) if pas_json.endswith('.json')]

    json_data = pandas.DataFrame(columns=['name', 'likes'])


    text = ''
    for d, x in enumerate(json_files):
        
        with open(os.path.join(path_json, x)) as json_file:

            json_text = json.load(json_file)
            

            name = json_text["username"]
            likes = [data["likes"] for data in json_text["posts"]]

            list_hastag = []
            for data in json_text["posts"]:
                for values in data["tags"]:

                    text += values.replace('#', ' ')
     
            total = 0

            for data in likes:
                total += data
        
            json_data.loc[d] = [name, total]
    
    work = WordCloud(max_font_size=40, background_color="white").generate(text)

    plt.figure()
    plt.imshow(work, interpolation='bilinear')
    plt.axis("off")
    plt.savefig('demol.png', bbox_inches='tight')

    data = {'{}'.format(json_data.iloc[data][0]):json_data.iloc[data][1] for data in range(len(json_data))}


    names = list(data.keys())
    value = list(data.values())


    fig, axs = plt.subplots(1, 1, figsize=(9, 3), sharey=True)
    axs.bar(names, value)
    fig.suptitle('Total Likes')
    plt.savefig('demo123.png', bbox_inches='tight')


if __name__ == '__main__':
    main()

    
# print(text)

