#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from BaseFunction.caculator import Caculator


class TestCalc:
    def setup_class(self):
        print("\n计算开始")
        self.calc = Caculator()


    def teardown_class(self):
        print("\n计算结束")

    @pytest.mark.parametrize(["a", "b", "expect"],
                             [[1, 1, 2], [1, 2, 4], [100000000000000, 100000000000000, 200000000000000], [0, 0, 0],
                              [0.1, 0.1, 0.2],
                              [-1, -1, -2]])
    def test_add(self, a, b, expect):
        result = self.calc.add(a, b)
        assert result == expect

    @pytest.mark.parametrize(["a", "b", "expect"],
                             [[1, 1, 1], [0.1, 0.1, 1], [0.1, 2, 0.05], [1, 2, 0.5], [10, 3, 3.3], [1, 3, 0.3],
                              [0, 0, 0]])
    def test_div(self, a, b, expect):
        if b == 0:
            print("被除数不可以为0")
        else:
            result = self.calc.div(a, b)
            assert result == expect
