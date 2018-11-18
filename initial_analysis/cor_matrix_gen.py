import pandas as pandas
import matplotlib.pyplot as plt


def load_data(data_file):
    data_dir = '../raw_data/'  + data_file
    match_data = pandas.read_csv(data_dir)

    return match_data

def save_coorelation_data(cm, out_dir):
    data_dir = 'output/' + out_dir + '_cormatrix.csv'

    cm.to_csv(data_dir)

def save_heatmap_data(out_dir):
    data_dir = 'output/' + out_dir + '_heatmap.png'
    plt.savefig(data_dir, bbox_inches='tight')


def generate(input_filename, output_filename):
    data = load_data(input_filename)
    correlation_matrix = data.corr()

    save_coorelation_data(correlation_matrix, output_filename)

    plt.matshow(correlation_matrix)

    save_heatmap_data(output_filename)