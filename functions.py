FILEPATH = "adatok.txt"

def get_adatok(filepath=FILEPATH):
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filepath, "r") as file_local:
        tevekenysegek_local = file_local.readlines()
    return tevekenysegek_local


def write_adatok(tevekenysegek_arg, filepath=FILEPATH):
    """ Write the to-do items list in the text file."""
    with open(filepath, "w") as file_local:
        file_local.writelines(tevekenysegek_arg)


