#!/usr/env/bin python

import ari_function, maddie_function, morgan_filter, write_rosie


if __name__ == "__main__":
	eq_cat = maddie_function.read_usgs("filename.csv")
	smaller_cat = morgan_filter.bounding_box(eq_cat, [-125, -115, 30, 40])
	write_rosie.write(smaller_cat, "smaller_file.txt")
