"""
    Modul nie spelniajacy zasady Liskov:
    klasy potomnej nie da sie podstawic w kazdym przypadku za klase bazowa!
"""


class NormalFile:

    def read(self):
        # read file implementation
        print('Reading from regular file')
 
    def write(self, input_text):
        # write file implementation
        print('Writing to regular file')
 
 
class ReadonlyFile(NormalFile):

    def read(self):
        # read readonly file implementation
        print('Reading from readonly file')
 
    def write(self, input_text):
        raise Exception('Can\'t write to readonly file')
 
 
normal_file = NormalFile()
readonly_file = ReadonlyFile()
 
 
def make_file_operations(file, input_text):
    if not isinstance(file, ReadonlyFile):
        file.write(input_text)
    # some processing stuff
    file.read()


make_file_operations(normal_file, 'tekst')
make_file_operations(readonly_file, 'tekst')
