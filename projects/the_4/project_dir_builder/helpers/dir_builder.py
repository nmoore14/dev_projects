import os

class Dir_Builder:

    def __init__(self, path, name, structure, system):
        self.path = path
        self.name = name
        self.structure = structure
        self.system = system
        self.sep = self.check_system(self.system)

    def check_system(self, system):
        if system == 'Windows':
            return "\\"
        else:
            return "/"

# TODO: Loop through the files in the current diretory, then proceed to the next directory

    def build_project(self, structure):
       # new_dir = self.path + self.sep + self.name
       # for key, value in self.structure.items():
       # TODO: Get the project structure
       # TODO: Loop through the structure
            # TODO: Create all of the files in the folder
            # TODO: Create all of the directories in the folder
                # TODO: If the directory has it's own structure, recall this loop

    def build_dir(self, path, name, structure):
        try:
            os.mkdir(path + self.sep + name)
            print("Directory created: " + name)
        except:
            print("Can't build new directory => " + name)

    def add_files(self, path, file_name):
        new_file = path + self.sep + file_name

        try:
            f = open(new_file, "w+")
            f.close()
            print("File created: " + file_name)
        except:
            print("Can't create file => " + file_name)

    def view_info(self):
        print("Debugging received info...")
        print("Path: " + self.path)
        print("Name: " + self.name)
        print("Structure: " + str(self.structure))
