import pytest
from psychopy.wizard import ConfigWizard, BenchmarkWizard

# py.test -k wizard --cov-report term-missing --cov wizard.py

@pytest.mark.wizard
class TestWizard():

    def setup(self):
        pass

    def teardown(self):
        pass

    def test_firstrunWizard(self):
        con = ConfigWizard(firstrun=False, interactive=False, log=False)
        result = open(con.reportPath, 'rU').read()
        assert 'This page auto-generated by the PsychoPy configuration wizard' in result

    def test_benchmarkWizard(self):
        ben = BenchmarkWizard(fullscr=False, interactive=False, log=False)
        result = open(ben.reportPath, 'rU').read()
        assert 'This page auto-generated by the PsychoPy configuration wizard' in result
