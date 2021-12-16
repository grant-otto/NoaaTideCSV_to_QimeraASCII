# NoaaTideCSV_to_QimeraASCII
Converter and example for quickly converting a NOAA Tide CSV to a CSV file supported by Qimera ASCII import.

Instructions for this converter:
1. Clone this repository.
2. Ensure you have set up a Python environment that uses Pandas and Numpy (Anaconda is an excellent resource)
3. Copy the files you want to convert into this folder. The code will convert all CSV files in this directory.
4. Run the noaaTideCSV_to_QimeraCSV.py Python file. 
5. Your new CSVs will appear with a new filename that includes the timestamp in the $converted_files$ folder.
6. In Qimera, import a custom ASCII file and select the converted file. For ease of use, you may load the ASCII file Config file supplied in this repository into the parser rather than setting the fields yourself.
