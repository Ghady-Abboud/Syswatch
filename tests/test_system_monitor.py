import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.system_monitor import (
    get_cpu_usage,
    get_memory_usage,
    get_cpu_load_average,
    get_cpu_temp,
)
class TestSystemMonitor(unittest.TestCase):

    def _assert_usage_value(self, get_usage_func):
        """Helper method to test usage functions that return percentage values"""
        usage = get_usage_func()
        self.assertIsInstance(usage, (int, float))
        self.assertGreaterEqual(usage, 0)
        self.assertLessEqual(usage, 100)

    def test_get_cpu_usage(self):
        self._assert_usage_value(get_cpu_usage)

    def test_get_memory_usage(self):
        self._assert_usage_value(get_memory_usage)

    def test_get_cpu_load_average(self):
        cpu_load_average = get_cpu_load_average()
        self.assertIsInstance(cpu_load_average,tuple)
        self.assertIsInstance(cpu_load_average[0],float)

    def test_get_cpu_temp(self):
       temp = get_cpu_temp()
       self.assertIsInstance(temp, dict)

       for core,value in temp.items():
           self.assertIn("Core",core)
           self.assertIsInstance(value, float)
           self.assertGreaterEqual(value, 0.0)
           self.assertLessEqual(value, 100.0)
