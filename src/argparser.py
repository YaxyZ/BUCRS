import argparse

def get_desktop_path():
    import os
    return os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

class ArgParser():
    
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='A cool software to backup your file in the coolest way ever')
        self.generate_arguments()
        
        
    def generate_arguments(self):
        self.parser.add_argument('path', type=str, help='Path of the file or directory to backup - Required')
        self.parser.add_argument('dest', type=str, nargs='?', help='Optional destination of the backup, defaults to Desktop', default=get_desktop_path())
        self.parser.add_argument('-v', '--version', action='version', version='BUCRS 1.0')
        self.parser.add_argument('-t', '--type', help="Compression file format, defaults to tar", nargs="?", default="tar")
    
    def parse_arguments(self):
        return self.parser.parse_args()

    


def main():
    parser = ArgParser()
    results = parser.parse_arguments()


if __name__ == '__main__':
    main()