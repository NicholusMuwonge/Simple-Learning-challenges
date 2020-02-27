from unittest import TestCase

string = "some like that"
def fill_spaces(string):
  string_list = list(string)
  new_string=""
  for i in string:
    if i.isspace():
      space_index=string_list.index(i)
      string_list[space_index]="%20"
  return(new_string.join(string_list))
    

class TestSpaces(TestCase):

  def test_that_spaces_are_detected(self):
    sample_string="do more work"
    response= fill_spaces(sample_string)
    self.assertEqual(response,"do%20more%20work")

if __name__=="__main__":
  tests=TestSpaces()
  tests.test_that_spaces_are_detected()
