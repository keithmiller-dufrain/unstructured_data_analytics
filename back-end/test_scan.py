import unittest
from pathlib import Path
from scan import get_file_creation_date
from scan import get_last_accessed_date
from scan import get_modification_date
from scan import get_file_owner
from scan import get_file_size
from scan import get_file_path
from scan import get_filename

class testScanFunctions(unittest.TestCase):
    def test_owner(self):
        # check if function can return owner/admin of the file
        self.assertEqual(get_file_owner('./requirements.txt'), 'fraserblack')
        # PASSING

    def test_modification(self):
        # check if the function returns the modification date of the file 
        self.assertEqual(get_modification_date('./requirements.txt'), '06/12/2019')
        # PASSING

    def test_creation_date(self):
        #check if the function returns the creation date of the file     
        self.assertEqual(get_file_creation_date('./requirements.txt'), '09/12/2019')
        # PASSING

    def test_accessed_date(self):
        #check if the function returns the accessed date of the file 
        self.assertEqual(get_last_accessed_date('./requirements.txt'), '10/12/2019')
        # PASSING

    def test_file_size(self):
        #check if the function returns the size of the file, this returns in bytes
        self.assertEqual(get_file_size('./requirements.txt'), 0)
        # PASSING

    #def test_get_file_path(self):
        # test if i can return a single file path
       # self.assertEquals(get_file_path(Path.cwd()), 1)

    def test_get_filename(self):
        # test if i can return the filename
        self.assertEqual(get_filename('./requirements.txt'), 'requirements.txt')


if __name__ == '__main__':
    unittest.main()