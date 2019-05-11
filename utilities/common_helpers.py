
import os
import re
import subprocess

from utilities.logging_manager import initialise_logging

logger = initialise_logging(__file__, "run.run_manager")


class FileOrDirectoryDoesNotExist(Exception):
    pass


def run_os_command(command):

    """
    Run given command on local operating system

    :param command:     Command to run

    """

    # Execute given command and store results
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output, error = process.communicate()
    return_code = process.returncode

    logger.debug(f"Return code: {return_code}")
    logger.debug(f"Standard output: {output.decode('utf-8')}")

    # Upon error, convert message from bytes to string and print result
    if error:
        logger.error(error.decode("utf-8"))


def fs_check_exists(command, file_path, error):

    """
    Execute a given command to check for a file's existence

    :param command:     Command to run
    :param file_path:   File path to check
    :param error:       Whether to raise an exception or simply return boolean outcome

    :return outcome:    Whether the file path exists

    """

    try:
        # Execute given command and evaluate output
        subprocess.check_output(command, shell=True, stderr=subprocess.PIPE)
        return True

    except subprocess.CalledProcessError:
        # Raise specific exception on error if desired, otherwise return false
        if error:
            raise FileOrDirectoryDoesNotExist(f"File or directory does not exist: {file_path}")
        return False


# Check whether file exists on HDFS
def fs_check_exists_hdfs(file_path, error = False):
    fs_check_exists(f"hdfs dfs -find {file_path}", file_path, error)


# Check whether file exists on local linux system
def fs_check_exists_local(file_path, error = False):
    fs_check_exists(f"find {file_path}", file_path, error)


# List full file path of all files within a given directory
def fs_list_directory_full_path(directory):
    return [os.path.join(directory, file) for file in os.listdir(directory)]


# Convert a camel case string to snake case
def string_camel_to_snake(camel_name):
    snake_name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', camel_name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', snake_name).lower().replace(" ", "_").replace("__", "_")


# Remove all special characters and replace ' ' with '_' within string
def string_remove_special_characters(complex_name):
    return re.sub("[^A-Za-z0-9_]", "", complex_name.replace(" ", "_")).lower()


def delete_keys_from_dict(dictionary, to_delete):

    """
    Remove keys from nested dictionaries without passing in full key path

    :param dictionary:  Dictionary to process
    :param to_delete:   Key(s) to remove from dictionary
    :return:            Dictionary with given keys removed

    """

    # Convert key to list
    if isinstance(to_delete, str):
        to_delete = [to_delete]

    # Process variable if dictionary
    if isinstance(dictionary, dict):

        # Iterate through keys, removing them from the given dictionary one by one
        for single_to_delete in set(to_delete):
            if single_to_delete in dictionary:
                del dictionary[single_to_delete]

        # Feed nested dictionaries (values) into same function
        for key, value in dictionary.items():
            delete_keys_from_dict(value, to_delete)

    # Feed each element of list into same function
    elif isinstance(dictionary, list):
        for index in dictionary:
            delete_keys_from_dict(index, to_delete)

    return dictionary
