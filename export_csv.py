#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv

from movie_export import MovieExport

if __name__ == '__main__':
    m = MovieExport("4523655")
    with open('movie_export.csv', mode='w') as movie_file:
        writer = csv.writer(movie_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for wish in m.get_wish():
            writer.writerow([wish.title, wish.url, wish.intro, wish.tags, wish.comment, wish.rating, wish.rating_date])