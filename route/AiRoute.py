import werkzeug
from flask_restful import reqparse, Resource

#route class
class AiRoute(Resource):
    def __init__(self, aiService):
        self.aiService = aiService  #initalize by DI
        
        #fashion item mapping
        self.resultMap = {
            '0':'T-shirt/top',
            '1':'Trouser',
            '2':'Pullover',
            '3':'Dress',
            '4':'Coat',
            '5':'Sandal',
            '6':'Shirt',
            '7':'Sneaker',
            '8':'Bag',
            '9':'Ankle boot'
        }

    def post(self):
        #prepare to read input body
        parser = reqparse.RequestParser()
        #add image attribute in request parser
        parser.add_argument('image',type=werkzeug.datastructures.FileStorage, location='files')
        parser.add_argument("class_id", type=int)

        #read upload image file
        args = parser.parse_args()
        imgFile = args['image']
        actualResultId = args.class_id


        #predict result by invoking trained model
        predictResultId = self.aiService.classify(imgFile)
        #convert to human readable description
        predictResultStr = self.resultMap[str(predictResultId)]

        # #prepare output result
        result = {
            'Predict Item Class':predictResultStr,
        }

        #compare result if user provide class id
        if not actualResultId:
            pass
        else:
            actualResultStr = self.resultMap[str(actualResultId)]

            if predictResultId == actualResultId:
                guessResult = 'Correct! Cheers~'
            else:
                guessResult = 'WRONG Guessing! Try another image.'
        
            result['Actual Item Class'] = actualResultStr
            result['Guess Result'] = guessResult

        print(f'Output Result: {result}')
        print('----------------------\n')
        return result, 201
