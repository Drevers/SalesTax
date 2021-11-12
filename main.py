import unittest
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
    __basic_sales_tax: float = 0.1
    __import_tax: float = 0.05

    @staticmethod
    def generate_receipt(items:list):
        raise NotImplementedError()

    @staticmethod
    def calculate_tax(item:Type[Item]) -> float:
        raise NotImplementedError()

class TestReceipt(unittest.TestCase):

    def test_exempt_goods(self):
        #test if the code can handle exempt goods
        book:Type[Item] = Item("book",12.49,1,True,False)
        cd:Type[Item] = Item("music cd",14.99,1,True,False)
        chocolate:Type[Item] = Item("chocolate bar",0.85,1,True,False)
        goods:list = [book,cd,chocolate]
        res = "1 book: 12.49\n 1 music CD: 16.49\n 1 chocolate bar: 0.85\n Sales Taxes: 1.50\n Total: 29.83"
        self.assertEqual(res,Receipt.generate_receipt(goods))

    def test_imported_goods(self):
        #test if the code can handle imported goods
        chocolate:Type[Item] = Item("imported box of chocolates",10.00,1,True,True)
        perfume:Type[Item] = Item("imported bottle of perfume",47.50,1,False,True)
        goods:list = [chocolate,perfume]
        res = "1 imported box of chocolates: 10.50\n 1 imported bottle of perfume: 54.65\n Sales Taxes: 7.65\n Total: 65.15"
        self.assertEqual(res,Receipt.generate_receipt(goods))

    def test_mixed_goods(self):
        #test if the code can handle mixed goods
        perfume_imported:Type[Item] = Item("imported bottle of perfume",27.99,1,False,True)
        perfume:Type[Item] = Item("bottle of perfume",18.99,1,False,True)
        pills:Type[Item] = Item("packet of headache pills",9.75,1,True,False)
        chocolate:Type[Item] = Item("imported box of chocolates",11.25,1,True,True)
        goods:list = [perfume_imported,perfume,pills,chocolate]
        res = "1 imported bottle of perfume: 32.19\n 1 bottle of perfume: 20.89\n 1 packet of headache pills: 9.75\n 1 imported box of chocolates: 11.85\n Sales Taxes: 6.70\n Total: 74.68"
        self.assertEqual(res,Receipt.generate_receipt(goods))



if __name__ == '__main__':
    unittest.main()
