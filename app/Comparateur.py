import os

class Comparateur:
    def __init__(self, dir1, dir2):
        self.dir1 = dir1
        self.dir2 = dir2
    
    def count_files(self, directory):
        count = 0
        for root, _, files in os.walk(directory):
            count += len(files)
        return count
    
    def compare(self):
        dir1_file_count = self.count_files(self.dir1)
        dir2_file_count = self.count_files(self.dir2)
        return dir1_file_count, dir2_file_count


if __name__ == "__main__":
    dir1 = "/home/celia/Bureau/mada_patch_0515"
    dir2 = "/home/celia/Public/imports-magmi/data/wacoal_nrm"
    
    comparator = Comparateur(dir1, dir2)
    count1, count2 = comparator.compare()
    
    print(f"Nombre de fichiers dans {dir1}: {count1}")
    print(f"Nombre de fichiers dans {dir2}: {count2}")