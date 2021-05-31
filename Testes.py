import unittest

from Temperatura import Temperatura

class TestTemperaturaCelsius(unittest.TestCase):
  def setUp(self):
    self.conversorTest = Temperatura('C', 10)

  def testCelsiusToKelvin(self):
    self.conversorTest.convert('K')

    self.assertEqual(self.conversorTest.escala,'K')
    self.assertEqual(self.conversorTest.temperatura, 0.00)

  def testCelsiusToFahrenheit(self):
    self.conversorTest.convert('F')

    self.assertEqual(self.conversorTest.escala,'F')
    self.assertEqual(self.conversorTest.temperatura, 50.00)

class TestTemperaturaFahrenheit(unittest.TestCase):

  def setUp(self):
    self.conversorTest = Temperatura('F', 32)

  def testFahrenheitToCelsius(self):
    self.conversorTest.convert('C')

    self.assertEqual(self.conversorTest.escala,'C')
    self.assertEqual(self.conversorTest.temperatura, 0)

  def testFahrenheitToKelvin(self):
    self.conversorTest.convert('K')

    self.assertEqual(self.conversorTest.escala,'K')
    self.assertEqual(self.conversorTest.temperatura, 273.15)

class TestTemperaturaKelvin(unittest.TestCase):

  def setUp(self):
    self.conversorTest = Temperatura('K', 300)

  def testKelvintToCelsius(self):
    self.conversorTest.convert('C')

    self.assertEqual(self.conversorTest.escala,'C')
    self.assertEqual(self.conversorTest.temperatura, 26.85)

  def testKelvinToFahrenheit(self):
    self.conversorTest.convert('F')

    self.assertEqual(self.conversorTest.escala,'F')
    self.assertEqual(self.conversorTest.temperatura, 80.3)

if __name__ == '__main__':
  # unittest.main(argv=['first-arg-is-ignored'], exit=False)
  suite = unittest.TestSuite()
  suite.addTest(TestTemperaturaCelsius('testCelsiusToKelvin'))
  result = unittest.TextTestRunner(verbosity=2).run(suite)
 
  if result.wasSuccessful():
    exit(0)
  else:
    exit(1)