import sys

class Redireact():
    '''redirects the output to different stream'''
    def __init__(self, new_stdout) -> None:
        self.new_stdout = new_stdout
    def __enter__(self):
        ''' This method is invoked when a class is called'''
        self.orig_stdout = sys.stdout
        sys.stdout = self.new_stdout
    def __exit__(self, exc_type, exc_value, exc_traceback):
        '''Invoke whne class exits caled before __del__'''
        sys.stdout = self.orig_stdout


def main():
    '''use with to manage a file access object '''
    with open('my_log.txt', 'at') as fobj:
        r = Redireact(fobj) # Redirect will use fobj as new standard output object
        with r: #use our class instance
            print(f'this output will be sent to the log text file')
        print(f'back to console')



if __name__ == '__main__':

    print(f'The standard output stream is {sys.stdout}')
    main()
    print(f'The standard output stream is back to {sys.stdout}')
