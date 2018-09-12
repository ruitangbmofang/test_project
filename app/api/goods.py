# -*- coding:utf-8 -*-
from flask import request, flash, jsonify, render_template, abort

from app.Forms.billsform import GoodsForm
from app.api.pagn import Pagination
from app.models import db
from app.models.bills import Goods
from app.api import api_bp
import copy


@api_bp.route('/tt/', methods=['GET'])
def hi():
    return "hello"


# @api_bp.route('/addgoods/', methods=['POST', 'GET'])
# def addgoods():
#     if request.method == "POST":
#         if request.form:
#             try:
#                 goods_para = Goods(name=request.form["name"], unit_price=request.form["unit_price"], num=request.form["num"])
#             except Exception, e:
#                 return u"物品名称错误"
#             if request.form.get("goods_content"):
#                 goods_para.goods_content = request.form["goods_content"]
#             if request.form.get("colour"):
#                 goods_para.colour = request.form["colour"]
#             if request.form.get("type"):
#                 goods_para.type = request.form["type"]
#             dict_goods = copy.deepcopy(goods_para.__dict__)
#             try:
#                 db.session.add(goods_para)
#                 db.session.commit()
#                 # print dict_goods
#                 del dict_goods["_sa_instance_state"]
#                 # print dict_goods
#                 succ_data = {"status": "0", "data": dict_goods}
#                 # print succ_data
#                 return jsonify(succ_data)
#             except Exception:
#                 return jsonify({"status": "-1", "message": u"数据库操作失败"})
#     else:
#         return jsonify({"status": "-1", "message": "不支持GET方式"})

@api_bp.route('/addgoods/', methods=['POST', 'GET'])
def addgoods():
    form = GoodsForm(request.form)
    if request.method == 'POST' and form.validate():
        # print '#########################################################'

        # print form.name.data, form.goods_content.data, form.colour.data, form.unit_price.data, form.num.data, form.type.data, form.status.data, form.bill_id.data
        goods = Goods(form.name.data, form.goods_content.data, form.colour.data, form.unit_price.data, form.num.data, form.type.data, form.status.data, form.bill_id.data)
        db.session.add(goods)
        db.session.commit()
        flash('you add successfull')

    else:
        print "error"
    return render_template('addgoods.html', form=form)


@api_bp.route("/goodslist/<int:bill_id>/", methods=['GET'])
@api_bp.route('/goodslist/', methods=['GET'])
def goods_list(bill_id = None):
    if not bill_id:
        goods = Goods.query.all()
        # print goods
        Gs = []
        for i in goods:
            Gs.append(i.__dict__)
            # print i.__dict__
        return render_template('/getgoods.html', gs=goods)
    else:
        goods = Goods.query.filter_by(bill_id=bill_id).all()
        print goods
        Gs = []
        for i in goods:
            Gs.append(i.__dict__)
        return str(goods)

PER_PAGE = 10


@api_bp.route('/getgoods/', defaults={'page': 1}, methods=['GET'])
@api_bp.route('/getgoods/page/<int:page>')
def getgoods():
    count = Goods.query.all.count()
    goods = Goods.query.all()
    if not goods and page != 1:
        abort(404)
    pagination = Pagination(page, PER_PAGE, count)
    return render_template('getgoods.html', pagination=pagination, goods=goods)



