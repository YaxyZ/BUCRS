import shutil
import errno

class Backup():

    def __init__(self,src,dst,file_type):
        self.src = src
        self.dst = dst
        self.file_type = file_type


    def moveMethod(self):
        try:
            shutil.move(f"{self.src}.{self.file_type}", self.dst) #(Original file, Copy Destination)
            print("File moved successfully.")
        except OSError as e:
            # If the error was caused because the source wasn't a directory
            if e.errno == errno.ENOTDIR:
                shutil.copy(f"{self.src}.{self.file_type}", self.dst)
            else:
                print('Directory not copied. Error: %s' % e) 


    def make_tarfile(self): #(Original file name, Original File Destination) *****call this function
        shutil.make_archive(self.src, self.file_type, self.src, verbose=True) #Makes the File into tar
        self.moveMethod()


def main():
    src=r"C:\Users\yarin\Desktop\test"
    dst=r"C:\Users\yarin\Desktop\Projects"
    file = Backup(src,dst,'tar')
    file.make_tarfile()
    

if __name__ == '__main__':
    main()
