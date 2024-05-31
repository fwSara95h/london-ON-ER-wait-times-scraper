import pandas as pd
import os


def log_data(row_data=None, headers=None, filename='logs_dump.csv'):
    '''
    This function logs data to a CSV file.
    A new file is created if necessary.
    Existing files are appended to.
    '''

    if row_data is None:
        row_data = []
    if headers is None:
        headers = ['Time', 'Status', 'Message', 'Details']

    # Ensure row_data is a list of lists
    if row_data and not isinstance(row_data[0], list):
        row_data = [row_data]

    # Convert row_data to a DataFrame
    df = pd.DataFrame(row_data, columns=headers)

    file_exists = os.path.isfile(filename)
    if file_exists:
        # Append to the file without headers
        df.to_csv(filename, mode='a', header=False, index=False)
    else:
        # Create a new file with headers
        df.to_csv(filename, mode='w', header=True, index=False)
