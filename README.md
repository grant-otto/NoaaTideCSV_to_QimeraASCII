# NoaaTideCSV_to_QimeraASCII
Converter and example for quickly converting a NOAA Tide CSV to a CSV file supported by Qimera ASCII import.

Instructions for this converter:
1. Clone this repository.
2. Ensure you have set up a Python environment that uses Pandas (Anaconda is an excellent resource)
3. Copy the file you want to convert into this folder.
4. Edit the noaaTideCSV_to_QimeraCSV.py Python file: set the _filename_ variable to the name of the file you want to convert.
5. Run the script.
6. Your new CSV will appear with a new filename that includes the timestamp in this folder.
7. In Qimera, import a custom ASCII file and select the converted file. For ease of use, you may load the ASCII file Config file supplied in this repository into the parser rather than setting the fields yourself.
