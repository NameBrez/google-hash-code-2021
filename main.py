from multiprocessing import Pool
from tqdm import tqdm

import pandas as pd
import numpy as np

# pools = Pool(processes=6)
# for ret_code, command in tqdm(pools.imap_unordered(pool_func_train, train), total=len(train)):

def read_input(filename):
    with open(filename,"r") as f:
        lines = [line.replace("\n","") for line in f.readlines()]
        line_1 = lines[0].split(" ")
        duration = int(line_1[0])
        n_intersections = int(line_1[1])
        intersections = list(range(n_intersections))
        n_streets = int(line_1[2])
        n_cars = int(line_1[3])
        bonus_points = int(line_1[4])

        streets = []
        for i in range(1, 1 + n_streets):
            street_data = lines[i].split(" ")
            inter_start = street_data[0]
            inter_end = street_data[1]
            street_name = street_data[2]
            street_duration = street_data[3]
            streets.append((inter_start, inter_end, street_name, street_duration))

        paths = []
        for i in range(1 + n_streets, 1 + n_streets + n_cars):
            path_data = lines[i].split(" ")
            paths.append(path_data[1:])


    return duration, intersections, streets, paths, bonus_points




if __name__ == '__main__':
    duration, intersections, streets, paths, bonus_points = read_input("data/a.txt")


