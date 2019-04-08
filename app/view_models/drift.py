

class DriftViewModel:
    def __init__(self,drift,current_user_id):
        self.data = {}

    @staticmethod
    def requeser_or_gifter(drift,current_user_id):
        if drift.requester_id ==current_user_id:
            you_are = 'requester'
        else:
            you_are = 'gifter'


    def __parse(self,drift,current_user_id):
        you_are = self.requeser_or_gifter(drift,current_user_id)
        r = {
            'drift_id': drift.id,
            'you_are': you_are,
            # 'book_title': drift.gift.book.title,
            # 'book_author': drift.gift.book.author_str,
            'book_title': drift.book_title,
            'book_author': drift.book_author,
            'book_img': drift.book_img,
            'operator': drift.requester_nickname if you_are != 'requester' \
                else drift.gifter_nickname,
            'date': drift.create_datetime.strftime('%Y-%m-%d'),
            'message': drift.message,
            'address': drift.address,
            'recipient_name': drift.recipient_name,
            'mobile': drift.mobile,
            # 'status_str': pending_status,
            'status': drift.pending
        }