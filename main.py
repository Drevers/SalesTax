from item import Item
from receipt import Receipt
import unittest

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
