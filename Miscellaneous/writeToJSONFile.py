import glob
import json
import os

# new_metadata_files = []


def get_metadata_files(path_metadata_dir):
    """ Generates a list of json-file-names in the directory path_metadata_dir. """
    os.chdir(path_metadata_dir)  # from directory with metadata json files
    metadata_files = [f for f in glob.glob("*.json")]  # list of file names with extension .json

    return metadata_files  # returns the list


def read_from_json(path_metadata_dir, file_name):
    """ Reads the content of a json file. """
    filePathName = path_metadata_dir + file_name
    with open(filePathName, 'r', encoding="utf-8") as f:
        content_to_save = json.loads(f.read())

    return content_to_save  # returns the JSONs content as a string


def write_to_new_json(path_new_dir, fname, data):
    """ Writes the content of one json-file into a new json-file. """
    filePathNameWExt = path_new_dir + '/' + fname
    with open(filePathNameWExt, 'w', encoding="utf-8") as new_f:
        json.dump(data, new_f)

    return new_f


def new_json_files(path_metadata_dir, path_new_dir):
    """ Generates the new metadata files list. """
    metadata_files = get_metadata_files(path_metadata_dir)
    for fname in metadata_files:
        content_json = read_from_json(path_metadata_dir, fname)
        fname = write_to_new_json(path_new_dir, fname, content_json)
        new_metadata_files.append(fname)

    return new_metadata_files


path_metadata_dir = './data/metadata/smarthub_nuance/skill-edge/'
path_new_dir = './data/metadata/smarthub_nuance/new_metadata/'

new_metadata_files = new_json_files(path_metadata_dir, path_new_dir)




# def get_data(configuration: Configuration):
#     """Loads the JSON file a parse the content for the used runner type and environment"""
#     skill_location, path, filename = get_file_details(configuration=configuration)
#
#     with open(skill_location, encoding="utf-8") as f:
#         data = f.read()
#         if not configuration.args.clone:
#             data = replace_with_real_data(configuration, data)
#
#         data = json.loads(data)
#
#     return skill_location, data

