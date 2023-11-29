import json
import csv
import sys
from pylatex import Document, Tabular, NoEscape, MultiRow, MultiColumn

#only works with one table, implement multiple later
#check stars are working correctly

def main(config_filepath, csv_filepath): 
	with open(config_filepath, 'r') as config_file: 
		config = json.load(config_file)

	with open(csv_filepath, 'r') as csv_file: 
		csv_reader = csv.reader(csv_file)
		next(csv_reader)

		doc = Document()

		num_tables = config["num_tables"]
		table_width = config["table_width"]
		table_names = config["table_names"]

		labels = config["labels"]
		data_cols = config["data_column"]
		se_cols = config["SE_column"]
		sig_cols = config["95sig"]
		sigTwo_cols = config["97.5sig"]
		sigThree_cols = config["99sig"]

		with doc.create(Tabular('l' + 'c'*(len(data_cols) + len(se_cols)), booktabs = True)) as table: 
			headers = ['']
			if num_tables > 1: 
				top = [MultiRow(2, data='Factor')]
				for table_name in table_names: 
					top.append(MultiColumn(table_width, align='c', data=table_name))
				table.add_row(top)

				table.add_hline(cmidruleoption='lr', start = 2, end = 1 + table_width)
				table.add_hline(cmidruleoption='lr', start = 2 + table_width, end = 1 + 2*table_width)
			else: 
				headers = ['Factor']

			for label in labels: 
				headers.append(NoEscape("${}$".format(label)))
				headers.append("SE")
			table.add_row(headers)
			table.add_hline()

			for row in csv_reader: 
				row_data = [row[1]]
				for i in range(len(data_cols)): 
					stars = "{{}}"
					entry = float(row[data_cols[i]])
					if (entry < 0 and entry < float(row[sigThree_cols[2*i]])) or (entry > 0 and entry > float(row[sigThree_cols[(2*i)+1]])):
						stars = "{{***}}"
					elif (entry < 0 and entry < float(row[sigTwo_cols[(2*i)]])) or (entry > 0 and entry > float(row[sigTwo_cols[(2*i)+1]])):
						stars = "{{**}}"
					elif (entry < 0 and entry < float(row[sig_cols[(2*i)]])) or (entry > 0 and entry > float(row[sig_cols[(2*i)+1]])):
						stars = "{{*}}"

					#change here to change number of decimals printed
					row_data.append(NoEscape("${:.2f}^{}$".format(entry, stars)))
					row_data.append(NoEscape("$({:.2f})$".format(float(row[se_cols[i]]))))
				table.add_row(row_data)

		doc.generate_tex("table")


if __name__ == "__main__": 
	argc = len(sys.argv)
	if argc != 3 : 
		print("Usage: python main.py <config_file> <csv_file>")
		sys.exit(1)

	main(sys.argv[1], sys.argv[2])