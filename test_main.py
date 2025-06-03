import project
import io
from unittest.mock import patch
import pytest
from contextlib import redirect_stdout

attributes = {"Age": '40', "Biological sex": 'female', "Height": '1.70', "Weight": '60', "Level of physical activity": 'lightly active'}

def test_greeting():
    f = io.StringIO()
    with redirect_stdout(f):
        project.greeting()
    output = f.getvalue()
    assert "This program will ask for your age" in output
    assert "Recommended daily water consumption" in output
    assert "Body mass index (BMI)" in output
    assert "Note: This is only an approximation" in output

def test_get_information_incorrect():
    with patch('builtins.input', side_effect=['cat']):
        with pytest.raises(SystemExit):
            project.get_information()
    with patch('builtins.input', side_effect=['-10']):
        with pytest.raises(SystemExit):
            project.get_information()
    with patch('builtins.input', side_effect=['18', 'cat']):
        with pytest.raises(SystemExit):
            project.get_information()
    with patch('builtins.input', side_effect=['18', '18']):
        with pytest.raises(SystemExit):
            project.get_information()
    with patch('builtins.input', side_effect=['18', 'male', '-10', '20', 'sedentary']):
        with pytest.raises(SystemExit):
            project.get_information()
    with patch('builtins.input', side_effect=['18', 'male', '10', '20', '23']):
        with pytest.raises(SystemExit):
            project.get_information()
    with patch('builtins.input', side_effect=['18', 'male', '10', '20', 'cat']):
        with pytest.raises(SystemExit):
            project.get_information()
    with patch('builtins.input', side_effect=['18', 'male', '10', 'cat', 'sedentary']):
        with pytest.raises(SystemExit):
            project.get_information()
    with patch('builtins.input', side_effect=['18', 'male', '10', '-10', 'sedentary']):
        with pytest.raises(SystemExit):
            project.get_information()

def test_get_information_correct():
    with patch('builtins.input', side_effect=['5', 'male', '1,65', '55,8', 'extremely active']):
        project.get_information()
    with patch('builtins.input', side_effect=['5', 'female', '1.65', '55.8', 'extremely active']):
        project.get_information()
    with patch('builtins.input', side_effect=['5', 'female', '1', '55', 'extremely active']):
        project.get_information()

def test_water():
    assert project.water(attributes) == 2.5
def test_bmi():
    assert project.bmi(attributes) == "normal weight"
def test_water():
    assert project.bmr(attributes) == 1301.5
def test_water():
    assert project.tdee(attributes) == 1789.56
