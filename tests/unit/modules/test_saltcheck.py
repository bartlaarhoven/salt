# -*- coding: utf-8 -*-

# Import python libs
from __future__ import absolute_import, print_function

# Import Salt Testing libs
from tests.support.unit import skipIf, TestCase
from salt.exceptions import CommandExecutionError

# Import salt libs
import salt.modules.saltcheck as saltcheck


class SaltCheckTestCase(TestCase):
    ''' SaltCheckTestCase'''

    def test_update_master_cache(self):
        self.assertTrue(saltcheck.update_master_cache)

    def test_call_salt_command(self):
        sc = saltcheck.SaltCheck()
        returned = sc.call_salt_command(fun="test.echo", args=['hello'], kwargs=None)
        self.assertEqual(returned, 'hello')

    #def test__is_valid_test(self):
    #    my_dict = {'module_and_function': 'test.echo',
    #                 'assertion': 'assertEqual',
    #                 'expected-return': 'True'}
    #    sc = saltcheck.SaltCheck()
    #    mybool = sc.__is_valid_test(my_dict)
    #    self.assertTrue(mybool)
        
    #def test_is_valid_module(self):
    #    sc = saltcheck.SaltCheck()
    #    returned = sc.is_valid_module('test')
    #    self.assertTrue(returned)

    def test__assert_equal1(self):
        sc = saltcheck.SaltCheck()
        a = {'a': 1, 'b': 2}
        b = {'a': 1, 'b': 2}
        mybool = sc._SaltCheck__assert_equal(a, b)
        self.assertTrue(mybool)

    def test__assert_equal2(self):
        sc = saltcheck.SaltCheck()
        a = {'a': 1, 'b': 2}
        b = {'a': 1, 'b': 2, 'c': 3}
        mybool = sc._SaltCheck__assert_equal(False, True)
        self.assertNotEqual(mybool, True)

    def test__assert_not_equal1(self):
        sc = saltcheck.SaltCheck()
        a = {'a': 1, 'b': 2}
        b = {'a': 1, 'b': 2, 'c': 3}
        mybool = sc._SaltCheck__assert_not_equal(a, b)
        self.assertTrue(mybool)

    def test__assert_not_equal2(self):
        sc = saltcheck.SaltCheck()
        a = {'a': 1, 'b': 2}
        b = {'a': 1, 'b': 2}
        mybool = sc._SaltCheck__assert_not_equal(a, b)
        self.assertNotEqual(mybool, True)

    def test__assert_true1(self):
        sc = saltcheck.SaltCheck()
        mybool = sc._SaltCheck__assert_equal(True, True)
        self.assertTrue(mybool)

    def test__assert_true2(self):
        sc = saltcheck.SaltCheck()
        mybool = sc._SaltCheck__assert_equal(False, True)
        self.assertNotEqual(mybool, True)

    def test__assert_false1(self):
        sc = saltcheck.SaltCheck()
        mybool = sc._SaltCheck__assert_false(False)
        self.assertTrue(mybool)

    def test__assert_false2(self):
        sc = saltcheck.SaltCheck()
        mybool = sc._SaltCheck__assert_false(True)
        self.assertNotEqual(mybool, True)

    def test__assert_in1(self):
        sc = saltcheck.SaltCheck()
        a = "bob"
        mylist = ['alice', 'bob', 'charles', 'dana']
        mybool = sc._SaltCheck__assert_in(a, mylist)
        self.assertTrue(mybool, True)

    def test__assert_in2(self):
        sc = saltcheck.SaltCheck()
        a = "elaine"
        mylist = ['alice', 'bob', 'charles', 'dana']
        mybool = sc._SaltCheck__assert_in(a, mylist)
        self.assertNotEqual(mybool, True)

    def test__assert_not_in1(self):
        sc = saltcheck.SaltCheck()
        a = "elaine"
        mylist = ['alice', 'bob', 'charles', 'dana']
        mybool = sc._SaltCheck__assert_not_in(a, mylist)
        self.assertTrue(mybool, True)

    def test__assert_not_in2(self):
        sc = saltcheck.SaltCheck()
        a = "bob"
        mylist = ['alice', 'bob', 'charles', 'dana']
        mybool = sc._SaltCheck__assert_not_in(a, mylist)
        self.assertNotEqual(mybool, True)

    def test__assert_greater1(self):
        sc = saltcheck.SaltCheck()
        a = 110
        b = 100
        mybool = sc._SaltCheck__assert_greater(a, b)
        self.assertTrue(mybool, True)

    def test__assert_greater2(self):
        sc = saltcheck.SaltCheck()
        a = 100
        b = 110
        mybool = sc._SaltCheck__assert_greater(a, b)
        self.assertNotEqual(mybool, True)

    def test__assert_greater3(self):
        sc = saltcheck.SaltCheck()
        a = 100
        b = 100
        mybool = sc._SaltCheck__assert_greater(a, b)
        self.assertNotEqual(mybool, True)

    def test__assert_greater_equal_equal1(self):
        sc = saltcheck.SaltCheck()
        a = 110
        b = 100
        mybool = sc._SaltCheck__assert_greater_equal(a, b)
        self.assertTrue(mybool, True)

    def test__assert_greater_equal2(self):
        sc = saltcheck.SaltCheck()
        a = 100
        b = 110
        mybool = sc._SaltCheck__assert_greater_equal(a, b)
        self.assertNotEqual(mybool, True)

    def test__assert_greater_equal3(self):
        sc = saltcheck.SaltCheck()
        a = 100
        b = 100
        mybool = sc._SaltCheck__assert_greater_equal(a, b)
        self.assertEqual(mybool, True)

    def test__assert_less1(self):
        sc = saltcheck.SaltCheck()
        a = 99
        b = 100
        mybool = sc._SaltCheck__assert_less(a, b)
        self.assertTrue(mybool, True)

    def test__assert_less2(self):
        sc = saltcheck.SaltCheck()
        a = 110
        b = 99
        mybool = sc._SaltCheck__assert_less(a, b)
        self.assertNotEqual(mybool, True)

    def test__assert_less3(self):
        sc = saltcheck.SaltCheck()
        a = 100
        b = 100
        mybool = sc._SaltCheck__assert_less(a, b)
        self.assertNotEqual(mybool, True)

    def test__assert_less_equal1(self):
        sc = saltcheck.SaltCheck()
        a = 99
        b = 100
        mybool = sc._SaltCheck__assert_less_equal(a, b)
        self.assertTrue(mybool, True)

    def test__assert_less_equal2(self):
        sc = saltcheck.SaltCheck()
        a = 110
        b = 99
        mybool = sc._SaltCheck__assert_less_equal(a, b)
        self.assertNotEqual(mybool, True)

    def test__assert_less_equal3(self):
        sc = saltcheck.SaltCheck()
        a = 100
        b = 100
        mybool = sc._SaltCheck__assert_less_equal(a, b)
        self.assertEqual(mybool, True)
