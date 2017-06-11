import re
import logging
import numpy as np
import pandas as pd
from collections import Counter


def clean_str(string):
    string = re.sub(r"[^A-Za-z0-9(),!?\'\`]", " ", string)
    string = re.sub(r"\'s", " \'s", string)
    string = re.sub(r"\'ve", " \'ve", string)
    string = re.sub(r"n\'t", " n\'t", string)
    string = re.sub(r"\'re", " \'re", string)
    string = re.sub(r"\'d", " \'d", string)
    string = re.sub(r"\'ll", " \'ll", string)
    string = re.sub(r",", " , ", string)
    string = re.sub(r"!", " ! ", string)
    string = re.sub(r"\(", " \( ", string)
    string = re.sub(r"\)", " \) ", string)
    string = re.sub(r"\?", " \? ", string)
    string = re.sub(r"\s{2,}", " ", string)
    return string.strip().lower()


def one_hot_encode(labels, label_dict):
    encoded_labels = []
    for label in labels:
        encoded_labels.append(label_dict[label])
    return encoded_labels


def load_data_and_labels():

    articles = np.load('data/bin/all_articles.npy')
    labels = np.load('data/bin/all_labels.npy')

    articles = [clean_str(article) for article in articles]

    # Map the actual labels to one hot labels
    label_list = sorted(list(set(labels)))
    one_hot = np.zeros((len(label_list), len(label_list)), int)
    np.fill_diagonal(one_hot, 1)
    label_dict = dict(zip(label_list, one_hot))

    labels = one_hot_encode(labels, label_dict)

    x_raw = articles
    y_raw = labels
    return x_raw, y_raw, label_list


def batch_iter(data, batch_size, num_epochs, shuffle=True):
    """Iterate the data batch by batch"""
    data = np.array(data)
    data_size = len(data)
    num_batches_per_epoch = int(data_size / batch_size) + 1

    for epoch in range(num_epochs):
        if shuffle:
            shuffle_indices = np.random.permutation(np.arange(data_size))
            shuffled_data = data[shuffle_indices]
        else:
            shuffled_data = data

        for batch_num in range(num_batches_per_epoch):
            start_index = batch_num * batch_size
            end_index = min((batch_num + 1) * batch_size, data_size)
            yield shuffled_data[start_index:end_index]


if __name__ == '__main__':
    load_data_and_labels()
