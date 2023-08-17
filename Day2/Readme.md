# Working with CSV Files in Machine Learning

CSV (Comma-Separated Values) files are a standard format for storing structured data, often used in machine learning projects. This guide provides an overview of various techniques and parameters you can use when working with CSV files in Python using the pandas library.

## Table of Contents

1. [Specifying Column Names and Separator](#specifying-column-names-and-separator)
2. [Changing the Index Column](#changing-the-index-column)
3. [Skipping Header Rows](#skipping-header-rows)
4. [Selecting Specific Columns](#selecting-specific-columns)
5. [Skipping Rows and Selecting Rows](#skipping-rows-and-selecting-rows)
6. [Encoding](#encoding)
7. [Handling Parser Errors](#handling-parser-errors)
8. [Data Types with dtype](#data-types-with-dtype)
9. [Handling Dates](#handling-dates)
10. [Using Converters](#using-converters)
11. [Handling Missing Values](#handling-missing-values)
12. [Loading Data in Chunks](#loading-data-in-chunks)

## 1. Specifying Column Names and Separator

By default, pandas assumes the first row of a CSV file to be column headers. If this is not the case, you can explicitly specify column names and separators.
### Example: Reading a TSV file with custom column names and separator

import pandas as pd
dff = pd.read_csv('/content/movie_titles_metadata.tsv', sep='\t', names=['serno','name','release year','ratings','votes','genres'])

## 2. Changing the Index Column
You can set a specific column as the index of the DataFrame using the index_col parameter.
### Example: Setting 'serno' as the index column

dff = pd.read_csv('/content/movie_titles_metadata.tsv', sep='\t', index_col='serno', names=['serno','name','release year','ratings','votes','genres'])

## 3. Skipping Header Rows
In some cases, the header row might not be the first row. You can skip header rows using the header parameter.
### Example: Skipping the first header row

df3 = pd.read_csv('/content/test.csv', header=1)

## 4. Selecting Specific Columns
To load only specific columns from a CSV file, you can use the usecols parameter.
### Example: Loading only 'enrollee_id' and 'gender' columns

selected_cols = pd.read_csv('/content/test.csv', header=1, usecols=['enrollee_id','gender'])

## 5. Skipping Rows and Selecting Rows
Use the skiprows and nrows parameters to skip rows at the beginning or select a specific number of rows.

## 6. Encoding
The encoding parameter specifies the character encoding of the CSV file. Common encodings are 'utf-8' and 'latin-1'.

## 7. Handling Parser Errors
In case your CSV file has inconsistent rows, you can use error_bad_lines=False to skip problematic lines.

## 8. Data Types with dtype
You can use the dtype parameter to explicitly specify the data types of the columns.

## 9. Handling Dates
The parse_dates parameter allows you to convert specified columns into datetime objects.

## 10. Using Converters
The converters parameter lets you apply custom functions to specific columns during data loading.

## 11. Handling Missing Values
The na_values parameter helps you identify and treat specified values as NaN (Not a Number) during loading.

## 12. Loading Data in Chunks
For large datasets, you can load data in smaller chunks using the chunksize parameter.
