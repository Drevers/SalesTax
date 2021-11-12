from item import Item
import math
from typing import Type

class Receipt:
    #class that allows us to create our receipts
    
    @staticmethod
    def generate_receipt(items:list):
        #generate the receipt string
        receipt: str = ""
        total_price: float = 0
        total_tax: float = 0
        for item in items: #create every single receipt line from the given quantity, name, price and tax
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
