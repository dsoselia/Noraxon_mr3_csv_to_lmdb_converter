# Noraxon_mr3_csv_to_lmdb_converter
This project helps convert from .csv exported from noraxon or nump0y arrays to lmdb

use:


for converting from csv:
place .csv(s) in csv_files directory
run transform.py

to convert from exisitng numpy arrays

use function merger.save_to_lmdb(x, y, name)
which takes X and y numpy arrays and name of the lmdb database ar arguments
