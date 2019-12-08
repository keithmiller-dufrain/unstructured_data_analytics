import unittest
from scan import get_file_creation_date
from scan import get_last_accessed_date
from scan import get_modification_date
from scan import get_file_owner
from scan import get_file_size
from scan import get_file_path

class testScanFunctions(unittest.TestCase):
    def test_owner(self):
        # check if function can return owner/admin of the file
        self.assertEquals(get_file_owner(pass in file), 'fraserblack')