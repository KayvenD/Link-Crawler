

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class printc:
    def warning(self):
        print(bcolors.WARNING)
        print(self)
        print(bcolors.ENDC)
    def failed(self):
        print(bcolors.FAIL)
        print(self)
        print(bcolors.ENDC)
    def success(self):
        print(bcolors.HEADER)
        print(self)
        print(bcolors.ENDC)