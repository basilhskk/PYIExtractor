import argparse

from lib.PyiArchive import  PyiArchive
from lib.logger import TerminalColors



def banner():
    print(TerminalColors.CYAN+"    ____ __  __ ____   ______       __                      __              "+TerminalColors.ENDC)
    print(TerminalColors.CYAN+"   / __ \\\\ \/ //  _/  / ____/_  __ / /_ _____ ____ _ _____ / /_ ____   _____"+TerminalColors.ENDC)
    print(TerminalColors.CYAN+"  / /_/ / \  / / /   / __/  | |/_// __// ___// __ `// ___// __// __ \\ / ___/"+TerminalColors.ENDC)
    print(TerminalColors.CYAN+" / ____/  / /_/ /   / /___ _>  < / /_ / /   / /_/ // /__ / /_ / /_/ // /    "+TerminalColors.ENDC)
    print(TerminalColors.CYAN+"/_/      /_//___/  /_____//_/|_| \__//_/    \__,_/ \___/ \__/ \____//_/     "+TerminalColors.ENDC)
                                                                            

def parse_args():

    usage_text = '''usage:

python3 pyiExtractor.py /path/to/exe

./pyiExtractor.py ../path/to/exe 
    '''

    parser = argparse.ArgumentParser(description='PyInstaller Source Extractor.')
    parser.add_argument('path', metavar='path', type=str, help='Path to PYInstaller Executable')
    
    return parser.parse_args()


if __name__ == "__main__":

    banner()

    args = parse_args()

    arch = PyiArchive(args.path)

    if arch.open():
        if arch.checkFile():
            if arch.getCArchiveInfo():
                arch.parseTOC()
                arch.extractFiles()
                arch.close()
                arch.logger.info('Successfully extracted pyinstaller archive: {0}'.format(args.path))
        arch.close()
