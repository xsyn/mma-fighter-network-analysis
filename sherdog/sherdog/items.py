# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class FightItem(Item):
    '''
    Should have all the fights with ID of "Fight N".
    There should be a FightItem() call for each fight.
    Dictionaries of all fights are then put in FighterItem().
    '''
    Verdict = Field()
    Opponent = Field()
    Event = Field()
    Date = Field()
    Method = Field()
    Round = Field()
    Time = Field()
    pass

class AttrItem(Item):
    '''
    Fighters attribute, one for each fighter.
    Dictionaries alongside dictionaries of fights.
    '''
    Birthday = Field()
    Weight = Field()
    Height = Field()
    Class = Field()
    Country = Field()
    pass

class FighterItem(Item):
    '''
    This is a superclass of FightItem and AttrItem so it binds both of them via
    dictionaries.
    '''
    Fights = Field()
    Bio = Field()
    pass
