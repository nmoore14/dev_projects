import os

class Dir_Builder:

    def __init__(self, path, name, structure):
        self.path = path
        self.name = name
        self.structure = structure

    def build_project(self):
        new_dir = self.path + "\\" + self.name
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
            os.mkdir(path + "\\" + name)
            print("Directory created: " + name)
        except:
            print("Can't build new directory => " + name)

    def add_files(self, path, file_name):
        new_file = path + "\\" + file_name

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
