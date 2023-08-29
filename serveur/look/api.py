from flask import request
from app import app
from discount.discountController import DiscountController
from discountType.discountTypeController import DiscountTypeController


@app.route('/discount_api', methods=['GET', 'POST', 'PUT', 'DELETE'])
def discountApi():
    controller=DiscountController()
    if request.method == 'POST':
        return controller.insertNewData()
    if request.method == 'GET':
        return controller.getData()
    if request.method == 'PUT':
        return controller.updateData()
    if request.method == 'DELETE':
        return controller.deleteData()
    return {'status':False, 'msg':'ínvalid http method'}

@app.post('/discount_api_search')
def discountApiSearch():
    return DiscountController().searchSingleData()

@app.get('/discount_type_api')
def discountTypeApi():
    return DiscountTypeController().getData()