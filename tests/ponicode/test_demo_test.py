import test_demo
import pytest

class Test_Testapp_Test_status_code:
    
    @pytest.fixture()
    def testapp(self):
        return test_demo.TestApp()
    

    def test_test_status_code_1(self, testapp):
        testapp.test_status_code()


class Test_Testapp_Test_message:
    
    @pytest.fixture()
    def testapp(self):
        return test_demo.TestApp()
    

    def test_test_message_1(self, testapp):
        result = testapp.test_message()

