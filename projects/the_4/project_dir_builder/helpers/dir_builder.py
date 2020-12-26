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

    def build_project(self):
        new_dir = self.path + self.sep + self.name
        try:
            os.mkdir(new_dir)
            print("Parent directory created: " + self.name)
            for key, value in self.structure.items():
                if key == 'files':
                    for f in value:
                        self.add_files(new_dir, f)
                else:
                    break
        except:
            print("Can't build new directory => " + self.name)

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
        print("Path: " + self.path)
        print("Name: " + self.name)
        print("Structure: " + str(self.structure))
