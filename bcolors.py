class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''

def printw(str):
	print(bcolors.WARNING + str + bcolors.ENDC)

def printe(str):
	print(bcolors.FAIL + str + bcolors.ENDC)

def prints(str):
	print(bcolors.OKGREEN + str + bcolors.ENDC)