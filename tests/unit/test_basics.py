import unittest

from mock import Mock

from virtualreality import VRBlock

from xblock.field_data import DictFieldData


class TestVRBlock(unittest.TestCase):
    """
    Tests for the Virtual Reality XBlock
    """
    def setUp(self):
        super(TestVRBlock, self).setUp()
        self.runtime = Mock()
        self.vr_data = {
            "title": "Test Title",
            "description": "Test Description",
            "embed_code": "https://player.vimeo.com/video/207466022",
            "highres_url": "https://player.vimeo.com/video/207466022",
            "lowres_url": "https://player.vimeo.com/video/207466022"
        }
        self.vr_block = VRBlock(
            self.runtime,
            DictFieldData(self.vr_data),
            None
        )

    def test_student_view_data(self):
        """
        Test the results of student_view_data
        """
        student_view_data = self.vr_block.student_view_data()
        self.assertEqual(student_view_data, self.vr_data)
