import unittest
import math
from typing import Type

class Item:
    #class of purchasable goods. requires the user to at least specify a price.
    #optionally users can also provide an amount, tax exemption and the import status
    def __init__(self,name:str,price:float,amount:int=1,exempt:bool=False,imported_good:bool=False):
        self.__name: str = name
        self.__price: float = price
        self.__amount: int = amount
        self.__exempt: bool = exempt
        self.__imported_good: bool = imported_good
    def get_name(self) -> str:
        return self.__name
    def get_price(self) -> float:
        return self.__price
    def get_amount(self) -> int:
        return self.__amount
    def is_exempt(self) -> bool:
        return self.__exempt
    def is_imported(self) -> bool:
        return self.__imported_good
    def set_name(self,name:str) -> None:
        self.__name = name
    def set_price(self,price:float) -> None:
        self.__price = price
    def set_amount(self,amount:int) -> None:
        self.__amount = amount
    def set_exempt(self,exempt:bool) -> None:
        self.__exempt = exempt
    def set_imported(self,imported_good:bool) -> None:
        self.__imported_good == imported_good

class Receipt:
    @staticmethod
    def generate_receipt(items:list):
        #generate the receipt string
        receipt: str = ""
        total_price: float = 0
        total_tax: float = 0
        for item in items:
            item_tax: float = Receipt.calculate_tax(item)
            total_tax += item_tax
            item_price: float = item.get_amount()*item.get_price() + item_tax
            total_price += item_price
            receipt += str(item.get_amount()) + " " + str(item.get_name()) + ": " + f"{item_price:.2f}" + "\n"
        receipt += "Sales Taxes: " + f"{total_tax:.2f}" + "\n"
        receipt += "Total: " + f"{total_price:.2f}"
        return receipt

    @staticmethod
    def calculate_tax(item:Type[Item]) -> float:
        #calculate the resulting tax for a given item
        tax: float = 0.10
        res: float = 0
        if (item.is_exempt()):
            tax = 0.00
        if (item.is_imported()):
            tax += 0.05
        res = item.get_amount()*item.get_price()*tax
        return Receipt.round(res)

    @staticmethod
    def round(num:float) -> float:
        #round the given number in accordance to the challenge's rules
        return math.ceil(num*20.00)/20.00

class TestReceipt(unittest.TestCase):

    def test_normal_exempt_goods(self):
        #test if the code can handle normal and exempt goods
        book:Type[Item] = Item("book",12.49,1,True,False)
        cd:Type[Item] = Item("music CD",14.99,1,False,False)
        chocolate:Type[Item] = Item("chocolate bar",0.85,1,True,False)
        goods:list = [book,cd,chocolate]
        res = "1 book: 12.49\n1 music CD: 16.49\n1 chocolate bar: 0.85\nSales Taxes: 1.50\nTotal: 29.83"
        self.assertEqual(res,Receipt.generate_receipt(goods))

    def test_exempt_imported_goods(self):
        #test if the code can handle exepmt and imported goods
        chocolate:Type[Item] = Item("imported box of chocolates",10.00,1,True,True)
        perfume:Type[Item] = Item("imported bottle of perfume",47.50,1,False,True)
        goods:list = [chocolate,perfume]
        res = "1 imported box of chocolates: 10.50\n1 imported bottle of perfume: 54.65\nSales Taxes: 7.65\nTotal: 65.15"
        self.assertEqual(res,Receipt.generate_receipt(goods))

    def test_normal_exempt_imported_goods(self):
        #test if the code can handle normal, exempt and imported goods
        perfume_imported:Type[Item] = Item("imported bottle of perfume",27.99,1,False,True)
        perfume:Type[Item] = Item("bottle of perfume",18.99,1,False,False)
        pills:Type[Item] = Item("packet of headache pills",9.75,1,True,False)
        chocolate:Type[Item] = Item("imported box of chocolates",11.25,1,True,True)
        goods:list = [perfume_imported,perfume,pills,chocolate]
        res = "1 imported bottle of perfume: 32.19\n1 bottle of perfume: 20.89\n1 packet of headache pills: 9.75\n1 imported box of chocolates: 11.85\nSales Taxes: 6.70\nTotal: 74.68"
        self.assertEqual(res,Receipt.generate_receipt(goods))



if __name__ == '__main__':
    unittest.main()
