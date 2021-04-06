import importlib

if __name__ == '__main__':
    module = importlib.import_module('dynamic_module.a.test_a')
    TestA = getattr(module, 'TestA')
    test_a = TestA()
    test_a.print_message()