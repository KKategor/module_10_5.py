# Task "Многопроцессное программирование"

from datetime import datetime
from multiprocessing import Pool

def read_info(filename):
    data = []
    with open (filename, 'r', encoding= 'utf-8') as file:
        for line in file:
            data.append(line)
    return data

if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    start_time = datetime.now()
    linear_data = []
    for filename in filenames:
        linear_data.extend(read_info(filename))
    print(datetime.now() - start_time, 'линейный метод')

    start_time = datetime.now()
    with Pool(processes=4) as pool:
        all_data = pool.map(read_info, filenames)
    combined_data = [line for data in all_data for line in data]
    print(datetime.now() - start_time, 'многопроцессный метод')
