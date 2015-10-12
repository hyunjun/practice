class Customer:
  def order(self, menuName, menu, barista):
    menuItem = menu.choose(menuName)
    coffee = barista.makeCoffee(menuItem)
    return coffee


class Menu:
  def __init__(self):
    self.items = [MenuItem("Americano", 1),
                  MenuItem("Cappuccino", 1.5),
                  MenuItem("Caramel Macchiato", 2),
                  MenuItem("Espresso", 1.2)]
  def choose(self, name):
    for item in self.items:
      if item.name == name:
        return item
    return None


class Barista:
  def makeCoffee(self, menuItem):
    coffee = Coffee(menuItem)
    return coffee


class Coffee:
  def __init__(self, menuItem):
    self.name = menuItem.getName()
    self.price = menuItem.cost()
  def __str__(self):
    return '{} / ${}'.format(self.name, self.price)


class MenuItem:
  def __init__(self, name, price):
    self.name = name
    self.price = price
  def cost(self):
    return self.price
  def getName(self):
    return self.name


if __name__ == '__main__':
  menu, barista, customer = Menu(), Barista(), Customer()
  print customer.order("Americano", menu, barista)
  print customer.order("Cappuccino", menu, barista)
  print customer.order("Caramel Macchiato", menu, barista)
  print customer.order("Espresso", menu, barista)
