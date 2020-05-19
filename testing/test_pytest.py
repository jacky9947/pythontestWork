
# -*- coding: utf-8 -*-
from python.calc import Calc
import sys
import yaml
import pytest
import allure
from  decimal import Decimal
sys.path.append("..")
class YamlData:
    def __init__(self,data_path):
        with open(data_path) as f:
            self.data=yaml.safe_load(f)
    def get_data(self,name):
        return self.data[name]
def steps(data_path1):
    with open(data_path1) as f:
        return yaml.safe_load(f)


add_data = YamlData('../datas/infodatas/add.yaml')
div_data = YamlData('../datas/infodatas/div.yaml')
sub_data=YamlData('../datas/infodatas/sub.yaml')
mul_data=YamlData('../datas/infodatas/mul.yaml')
step1 = steps('../datas/stepdatas/calc.yaml')


class TestCalc:
    def setup(self):
        self.calc = Calc()

    @pytest.mark.parametrize('test_data', add_data.get_data("norm"))
    @pytest.mark.run(order=2)
    @allure.step("测试加法函数")
    def test_add_1(self,test_data):
        print(step1)

        if 'add' in step1:
            result = self.calc.add(test_data['a'], test_data['b'])
            print(test_data['a'])
            print(test_data['b'])
            print(result)
            assert test_data['res']-result<0.0001

    @pytest.mark.parametrize('test_data', sub_data.get_data("norm"))
    @allure.step("测试减法函数")
    def test_sub_1(self, test_data):
        print(step1)

        if 'sub' in step1:
            result = self.calc.sub(test_data['a'], test_data['b'])
            print(test_data['a'])
            print(test_data['b'])
            print(result)
            assert test_data['res'] - result < 0.0001

    @pytest.mark.parametrize('test_data', mul_data.get_data("norm"))
    @allure.step("测试乘法函数")
    def test_mul_1(self, test_data):
        print(step1)

        if 'mul' in step1:
            result = self.calc.mul(test_data['a'], test_data['b'])
            print(test_data['a'])
            print(test_data['b'])
            print(result)
            assert test_data['res'] - result < 0.0001

    @pytest.mark.parametrize('test_data', div_data.get_data("norm"))
    @pytest.mark.run(order=1)
    @allure.step("测试除法函数")
    def test_div_1(self,test_data):
        print(step1)
        for step in step1:
            print(f"step ==== > {step}")
            if 'div' in step1:
                try:
                    result = self.calc.div(test_data['a'], test_data['b'])
                    print(test_data['a'])
                    print(test_data['b'])
                    print(result)
                except ZeroDivisionError:
                    print("0不能做除数")
                assert test_data['res']-result<0.0001
if __name__ == '__main__':
   # pytest.main(['-vs','test_pytest.py::TestCalc::test_div_1','test_pytest.py::TestCalc::test_add_1'])
    #pytest.main()
    pytest.main()