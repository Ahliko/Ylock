from utilities.response import Response
from discountType.discountTypeModel import DiscountType, DiscountTypeSchema


class DiscountTypeController:
    def __init__(self):
        super().__init__()
        self.dataHandler = DataHandlerImpl()

    def getData(self):
        try:
            data = self.dataHandler.getData()
            return Response.make(True, data=data)
        except:
            return Response.make(False, 'Error while trying to retrieve data')


class DataHandlerImpl:
    def __init__(self):
        super().__init__()
        self.Model = DiscountType
        self.Schema = DiscountTypeSchema

    def getData(self):
        objectResults = self.Model.query.all()
        return self.Schema(many=True).dump(objectResults)
