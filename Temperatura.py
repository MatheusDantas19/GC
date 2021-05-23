class Temperatura:
  def __init__(self, escala, temperatura):
    self.escala = escala
    self.temperatura = temperatura
  
  def celsiusToKelvin(self):
    self.escala = 'K'
    self.temperatura += 273.15

    print('Temperatura: ', round(self.temperatura,2), self.escala)
  
  def kelvinToCelsius(self):
    self.escala = 'C'
    self.temperatura -= 273.15

    print('Temperatura: ', round(self.temperatura,2), self.escala)

  def celsiusToFahrenheit(self):
    
    self.temperatura = (1.8 * self.temperatura) + 32.0;
    self.escala = 'F'

    print('Temperatura: ', round(self.temperatura,2), self.escala)

  def fahrenheitToCelsius(self):
    self.temperatura = (self.temperatura - 32.0) / 1.8
    self.escala = 'C'

    print('Temperatura: ', round(self.temperatura,2), self.escala)

  def kelvinToFahrenheit(self):
    self.temperatura = (self.temperatura * 1.8 - 459.7)
    self.escala = 'F'

    print('Temperatura: ', round(self.temperatura,2), self.escala)

  def fahrenheitToKelvin(self):
    self.temperatura = ((self.temperatura - 32) / 1.8 + 273.15)
    self.escala = 'K'

    print('Temperatura: ', round(self.temperatura,2), self.escala)

  def convert(self, escala):
    print("Convertendo...")
    if (escala == 'C'):
      if (self.escala == 'K'):
        self.kelvinToCelsius()
      elif (self.escala =='F'): 
        self.fahrenheitToCelsius();
      self.temperatura = round(self.temperatura,2)

    if (escala == 'K'):
      if (self.escala == 'C'): 
        self.celsiusToKelvin();
      elif (self.escala == 'F'): 
        self.fahrenheitToKelvin();
      self.temperatura = round(self.temperatura,2)

    if (escala == 'F'):
      if (self.escala == 'C'):
        self.celsiusToFahrenheit();
      elif (self.escala == 'K'): 
        self.kelvinToFahrenheit();
      
      self.temperatura = round(self.temperatura,2)

        
if __name__ == '__main__':
  Temp = Temperatura('K',300)
  Temp.convert('F')

