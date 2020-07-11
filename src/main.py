import shutil
import errno


def moveMethod(src,dst):
    try:
        shutil.move(src, dst) #(Original file, Copy Destination)
    except OSError as e:
        # If the error was caused because the source wasn't a directory
        if e.errno == errno.ENOTDIR:
            shutil.copy(src, dst)
        else:
            print('Directory not copied. Error: %s' % e)


def make_tarfile(source_dir,file_destination): #(Original file name, Original File Destination)
    file_type = 'tar'
    shutil.make_archive(source_dir, file_type, source_dir, verbose=True) #Makes the File into tar
    moveMethod(f"{source_dir}.{file_type}" ,file_destination)


def main():
    src=r"C:\Users\yarin\Desktop\test"
    dst=r"C:\Users\yarin\Desktop\Projects"
    make_tarfile(src,dst)
    

if __name__ == '__main__':
    main()
