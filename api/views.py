from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import pickle

class Generator(APIView):
    def generate(N,P,K,temperature,humidity,ph,rainfall):
        with open('api/crop_recomendation_model.pickle','rb') as f:
            model = pickle.load(f)
        return model.predict([[N,P,K,temperature,humidity,ph,rainfall]])

    def get(self, request):
        return Response("Request for Data")

    def post(self, request):
        
        data = request.data
        N = data['N']
        P = data['P']	
        K = data['K']
        temperature = data['temperature']	
        humidity = data['humidity']	
        ph = data['ph']	
        rainfall = data['rainfall']

        targets = {
            0: 'barley ',
            1: 'cotton ',
            2: 'guar',
            3: 'moong',
            4: 'mustard',
            5: 'sugarcane',
            6: 'wheat'}
        
        with open('api/crop_recomendation_model.pickle','rb') as f:
            model = pickle.load(f)
        result = model.predict([[N,P,K,temperature,humidity,ph,rainfall]])

        return Response(targets[result[0]])

        # except Exception as e:
        #     return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
# {
# "N":90,
# "P":42,
# "K":43,
# "temperature":20.87974371,
# "humidity":82.00274423,
# "ph":6.502985292000001,
# "rainfall":202.9355362
# }