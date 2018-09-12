# -*- coding:utf-8 -*-
from wtforms import Form, FloatField, StringField, IntegerField, validators, ValidationError


class GoodsForm(Form):
    name = StringField('name', [validators.Length(min=6, max=50, message=u"物品名称长度为6--50")])
    # name = StringField('name', [validators.Length(min=6, max=50)])
    goods_content = StringField('goods_content', [validators.Length(max=500, message=u"物品描述最大500个字")])
    colour = StringField('colour', [validators.Length(max=20, message=u"颜色长度最大20个字")])
    unit_price = FloatField('unit_price')
    num = IntegerField('num')
    type = IntegerField('type', [validators.Optional()])
    status = IntegerField('status', [validators.Optional()])
    bill_id = IntegerField('bill_id', [validators.Optional()])

    # 自定义字段验证
    # def validate_unit_price(form, field):
    #     if type(field.data) != float:
    #         raise ValidationError(u'单价应该是浮点数')

