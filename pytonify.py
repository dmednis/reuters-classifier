import json
import numpy as np
import os
from collections import Counter
import pprint
pp = pprint.PrettyPrinter(indent=4)


def read_files():
    jsondir = 'data/json'
    files = os.listdir(jsondir)
    all_data = []

    for filename in files:
        with open(jsondir + '/' + filename) as file:
            data = json.load(file)
        all_data.extend(data)

    return all_data


raw_data = read_files()

train_articles = []
train_labels = []
test_articles = []
test_labels = []
all_articles = []
all_labels = []

label_counts = {}

for item in raw_data:
    if item['topic'] in label_counts:
        label_counts[item['topic']] += 1
    else:
        label_counts[item['topic']] = 1

top_label_counts = Counter(label_counts).most_common(6)

top_labels = []

for count in top_label_counts:
    top_labels.append(count[0])


for item in raw_data:
    if item['topic'] in top_labels:
        if item['testing']:
            test_articles.append(item['body'])
            test_labels.append(item['topic'])
        else:
            train_articles.append(item['body'])
            train_labels.append(item['topic'])
        all_articles.append(item['body'])
        all_labels.append(item['topic'])

out_dir = 'data/bin'

np.save(out_dir + '/test_articles', test_articles)
np.save(out_dir + '/test_labels', test_labels)
np.save(out_dir + '/train_articles', train_articles)
np.save(out_dir + '/train_labels', train_labels)
np.save(out_dir + '/all_articles', all_articles)
np.save(out_dir + '/all_labels', all_labels)
