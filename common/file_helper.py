

def save_dataframe_to_file(dataframe, file_path, header = None):

    """
    Save pandas dataframe to given file path

    :param dataframe:   Pandas dataframe
    :param file_path:   Target file path
    :param header:      List of header columns

    """

    if header:
        dataframe.to_csv(
            path_or_buf = file_path,
            header = header,
            mode = "w+"
        )

    else:
        dataframe.to_csv(
            path_or_buf = file_path,
            mode = "w+"
        )
