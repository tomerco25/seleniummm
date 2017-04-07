from runp import runp
import os
import sys
import unittest


class RunPTestCase(unittest.TestCase):
    def setUp(self):
        self.test_path = os.path.dirname(os.path.abspath(__file__))
        self.runfile = os.path.join(self.test_path, "testfile.py")
        self.imported_vars = runp.load_runfile(self.runfile)
        self.functions = runp.filter_vars(self.imported_vars)

    def test_load_runfile(self):
        self.assertTrue(len(self.imported_vars) >= len(self.functions))

    def test_filter_vars(self):
        self.assertEquals(len(self.functions), 4)

    def test_print_functions(self):
        out = """Available functions:
Wip.print_it\t
wat\tWEEE
wet\t
wut\tSuper docstring test"""
        runp.print_functions(self.functions)
        output = sys.stdout.getvalue().strip()
        self.assertEquals(str(output), out)

    def test_print_function_no_docstring(self):
        out = """Displaying docstring for function wet in module testfile
wet()"""
        runp.print_function(self.functions, "wet")
        output = sys.stdout.getvalue().strip()
        self.assertEquals(str(output), out)

    def test_print_function_multi_docstring(self):
        out = """Displaying docstring for function wut in module testfile
wut(text, woop=False)
    Super docstring test

    Args:
        text (str): The text to print
        woop (boolean, optional): Default false"""
        runp.print_function(self.functions, "wut")
        output = sys.stdout.getvalue().strip()
        self.assertEquals(str(output), out)

    def test_run_function_noargs(self):
        out = "testing, 1, 2, 3"
        runp.run_function(self.functions, "wat")
        output = sys.stdout.getvalue().strip()
        self.assertEquals(str(output), out)

    def test_run_function_args(self):
        out = "mytext\ndoobey"
        runp.run_function(self.functions, "wut:mytext,doobey")
        output = sys.stdout.getvalue().strip()
        self.assertEquals(str(output), out)

    def test_run_function_named_args(self):
        out = "mytext\nTrue"
        runp.run_function(self.functions, "wut:mytext,woop=True")
        output = sys.stdout.getvalue().strip()
        self.assertEquals(str(output), out)

    def test_run_function_reverse_args(self):
        out = "mytext\nTrue"
        runp.run_function(self.functions, "wut:woop=True,mytext")
        output = sys.stdout.getvalue().strip()
        self.assertEquals(str(output), out)

    def test_run_function_wrong_args(self):
        out = "wut() takes at least 1 argument (0 given)"
        runp.run_function(self.functions, "wut")
        output = sys.stdout.getvalue().strip()
        self.assertEquals(str(output), out)

    def test_get_function_nonexistant(self):
        nofunc = "wutwut"
        out = "No function named '{}' found!".format(nofunc)
        runp.get_function(self.functions, nofunc)
        output = sys.stdout.getvalue().strip()
        self.assertEquals(str(output), out)

    def test_parse_args_noargs(self):
        inputstr = "wut"
        cmd, args, kwargs = runp.parse_args(inputstr)
        tup = (cmd, args, kwargs)
        self.assertEquals(tup, ("wut", [], {}))

    def test_parse_args_nokwargs(self):
        inputstr = "wut:wow,such,good"
        cmd, args, kwargs = runp.parse_args(inputstr)
        tup = (cmd, args, kwargs)
        self.assertEquals(tup, ("wut", ["wow", "such", "good"], {}))

    def test_parse_args(self):
        inputstr = "wut:arg=wow,'such spaces',arg2=good"
        cmd, args, kwargs = runp.parse_args(inputstr)
        tup = (cmd, args, kwargs)
        self.assertEquals(
            tup,
            ("wut", ["'such spaces'"], {"arg": "wow", "arg2": "good"})
        )

    def test_escape_split_comma(self):
        inputstr = "wut:arg=wow,'such spaces',arg2=good"
        splitted = ['wut:arg=wow', "'such spaces'", 'arg2=good']
        self.assertEquals(runp._escape_split(',', inputstr), splitted)

    def test_escape_split_equals(self):
        inputstrs = ['wut:arg=wow', "'such spaces'", 'arg2=good']
        results = [['wut:arg', 'wow'], ["'such spaces'"], ['arg2', 'good']]
        for i, inputstr in enumerate(inputstrs):
            self.assertEquals(runp._escape_split('=', inputstr), results[i])


if __name__ == '__main__':
    unittest.main()