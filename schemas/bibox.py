__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from marshmallow import (
    Schema,
    fields,
    pre_load,
    post_load
)
import settings as s


class Bibox(Schema):
    pair = fields.Str(required=True, attribute='symbol')
    source = fields.Str(required=True)
    last = fields.Float(required=True, attribute='price')
    vol = fields.Float(required=True, attribute='volume_24h')
    high = fields.Float(required=True, attribute='highest_price_24h')
    low = fields.Float(required=True, attribute='lowest_price_24h')

    @pre_load
    def pre_load(self, data):
        data['source'] = s.BIBOX
        return data

    @post_load
    def post_load(self, data):
        data['symbol'] = data['symbol'].replace('_', '')
        data['volume_24h'] = data['volume_24h'] * data['price']
        return data