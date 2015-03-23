#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CsvExtractor

Usage:
	csv_extractr.py <src_path> <target_path> <field> <pattern> [<replacement_str>]

Options:
	-h --help

Permet d'extraire / remplacer un motif d'un fichier csv, sur un field en particulier
"""

__all__ = ['handle_job']

from docopt import docopt
from ulv import Importer, Exporter
from os import remove


def handle_job():
	"""
		Parse CSV / replace <pattern> with <replacement_str> (or '' if doesn't attributed), for <field>
		in each row of <src_path> file, and output result in <target_path> file.
	"""
	# Gain args to parse
	args = docopt(__doc__)

	# Prepare CSV
	incsv = Importer(args['<src_path>'])
	outcsv = None

	# Loop on each row of input csv 
	for line in incsv.get_row_async():
		# build extracter
		if outcsv is None:
			outcsv = Exporter(args['<target_path>']+'.tmp', incsv.get_header())

		# Prepare replacement str, and default it.
		repl_str = ''
		if '<replacement_str>' in args and args['<replacement_str>'] is not None:
			repl_str = args['<replacement_str>'].encode().decode('unicode_escape')
		
		# Prepare pattern, and encode it for special char like '\n'
		pattern = args['<pattern>'].encode().decode('unicode_escape')

		# Replace pattern
		outfield = line[args['<field>']].replace(pattern, repl_str)
		line[args['<field>']] = outfield

		# Write it in output CSV
		outcsv.write_row(line)

	# Post clean File to fix Windows CSV bug 
	with open(args['<target_path>']+'.tmp', 'r') as tmpf, open(args['<target_path>'],'w') as outf:
		for line in tmpf:
			if line != '\n':
				outf.write(line)
	
	# remove tmp file
	remove(args['<target_path>']+'.tmp')


if __name__ == '__main__':
	# Main routine
	handle_job()