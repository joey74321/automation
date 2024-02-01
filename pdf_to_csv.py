# pdf_to_csv.py
import jpype
import tabula
import pandas as pd


def pdf_to_csv_function(pdf_path, csv_path):
    """
    Converts a PDF file to CSV.

    Parameters:
    - pdf_path (str): Path to the input PDF file.
    - csv_path (str): Path to save the output CSV file.
    """
    # Read PDF and extract tables
    tables = tabula.read_pdf(pdf_path, pages="all", multiple_tables=True)

    # Concatenate tables into a single DataFrame
    df = pd.concat(tables)

    # Save DataFrame to CSV
    df.to_csv(csv_path, index=False)


# Example usage:
if __name__ == "__main__":
    # Provide the path to the input PDF file and desired output CSV file
    input_pdf_path = "/Users/johvansalazar/Documents/MyCSV.pdf"
    output_csv_path = "/Users/johvansalazar/Documents/MyC"

    # Call the function to convert PDF to CSV
    pdf_to_csv_function(input_pdf_path, output_csv_path)
