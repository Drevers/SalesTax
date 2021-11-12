class Item:
    #class of purchasable goods. requires the user to at least specify a price.
    #optionally users can also provide an amount, tax exemption and the import status

    def __init__(self,name:str,price:float,amount:int=1,exempt:bool=False,imported_good:bool=False):
        self.__name: str = name
        self.__price: float = price
        self.__amount: int = amount
        self.__exempt: bool = exempt
        self.__imported_good: bool = imported_good

    #getter
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

    #setter
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
