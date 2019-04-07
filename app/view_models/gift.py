from .book import BookViewModel
from collections import namedtuple



# MyGift = namedtuple('MyGift',['id','book','wishes_count'])


class MyGifts:
    def __init__(self,gifts_of_mine,wish_count_list ):
        self.gifts = []

        self.__gifts_of_mine = gifts_of_mine
        self.__wish_count_list = wish_count_list

        self.gifts = self._parse()


    def _parse(self):
        temp = []
        for gift in self.__gifts_of_mine:
            my_gift =  self.__matching(gift)
            temp.append(my_gift)
        return temp



    def __matching(self,gift):
        count = 0
        for wish_count in self.__wish_count_list:
            if gift.isbn == wish_count['isbn']:
                count = wish_count['count']

        r = {
            'wishes_count':count,
            'book':BookViewModel(gift.book),
            'id':gift.id
        }
        return r
        # my_gift = MyGift(gift.id,BookViewModel(gift.book),count)
        # return my_gift


# class MyGift:
#     def __init__(self):
#