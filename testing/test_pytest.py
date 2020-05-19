#!/usr/bin/env python
# -*- coding: utf-8 -*-
from python.calc import Calc
import sys
import yaml
import pytest
from  decimal import Decimal
sys.path.append("..")
class YamlData:
    def __init__(self,data_path):
        with open(data_path) as f:
            self.data=yaml.safe_load(f)
    def get_data(self,name):
        return self.data[name]

add_data = YamlData('../datas/infodatas/add.yaml')
div_data = YamlData('../datas/infodatas/div.yaml')
steps = yaml.dump(YamlData('../datas/stepdatas/calc.yaml'))


class TestCalc:
    def setup(self):
        self.calc = Calc()

    @pytest.mark.parametrize('test_data', add_data.get_data("norm"))
    @pytest.mark.run(order=2)
    def test_add_1(self,test_data):

        result = self.calc.add(test_data['a'], test_data['b'])
        print(result)
        assert test_data['res']-result<0.000001


    @pytest.mark.parametrize('test_data', div_data.get_data("norm"))
    @pytest.mark.run(order=1)
    def test_div_1(self,test_data):

        result = self.calc.div(test_data['a'], test_data['b'])
        print(result)
        assert test_data['res']-result<0.000001
if __name__ == '__main__':
   # pytest.main(['-vs','test_pytest.py::TestCalc::test_div_1','test_pytest.py::TestCalc::test_add_1'])
    pytest.main()
    #pytest.main(["-vs", "-m", "add or div", "test_pytest.py"])