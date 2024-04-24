import unittest
from name_function import get_format_name, get_format_name2

class NameTestCase(unittest.TestCase):
  """ name_functionモジュールのテストクラス
  """

  def test_get_format_name(self):
      """get_format_name正常ケーステスト"""

      format_name = get_format_name("ryan", "howard")
      self.assertEqual(format_name, "Ryan Howard")

  def test_get_format_name2(self):
      """get_format_name正常ケーステスト"""

      format_name = get_format_name2("ryan", "howard", "")
      self.assertEqual(format_name, "Ryan Howard")

  def test_get_format_name2_1(self):
      """get_format_name正常ケーステスト"""

      format_name = get_format_name2("ryan", "howard", "ghost")
      self.assertEqual(format_name, "Ryan Ghost Howard")

if __name__ == '__main__':
    unittest.main()