from scrapy.item import Item, Field

class SherdogItem(Item):
    '''
    Defines the sturcture of the MMA fighters in the Sherdog database.
    Each item is taken after scrapy has done its work.
    '''
    
