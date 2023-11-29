## Usage

`python main.py <config_file> <csv_file>`

`config.json` should be changed prior to running the program. A brief overview of the different options is given below: 

`num_tables`: the number of tables being created. For example, to create the example table given in the slides, `num_tables=2`

`table_width`: how wide, in columns, each table should be

`table_names`: the names of the different tables. If `num_tables=0`, then this value can be anything

`label_column`: the index, with indexing starting from 0, of the column containing the row labels

`data_column`: an array containing the indices of columns containing the data of interest

`labels`: the column names for the columns in `data_column`, written in LaTeX

`SE_column`: an array containing the indices of columns containing the standard errors

`95sig`: array containing the indices of columns containing the 5 and 95 percent significance thresholds 

`97.5sig`: array containing the indices of columns containing the 2.5 and 97.5 percent significance thresholds 

`99sig`: array containing the indices of columns containing the .5 and 99.5 percent significance thresholds 

