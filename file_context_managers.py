class Open_file():

    # init method runs when object is created
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        print("__init__")

    # enter method runs when an operation such as a write is performed
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        print("__enter__")
        return self.file

    # exit method runs when an operation has finshed
    def __exit__(self, exc_type, exc_cal, traceback):
        print("__exit__")
        self.file.close()