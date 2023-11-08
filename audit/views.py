from rest_framework.decorators import api_view
from rest_framework import status
import openai
from rest_framework.response import Response
from openai import api_key
import requests

from rest_framework.response import Response
from .models import Facility, EnergyDevice, EnergyAudit
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from .serializers import FacilitySerializer, EnergyDeviceSerializer, EnergyAuditSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_facility(request):
    serializer = FacilitySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_energy_device(request):
    serializer = EnergyDeviceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)



@api_view(['POST'])
def create_energy_audit(request):
    if request.method == 'POST':
        facility_id = request.data.get( 'facility')
        devices_data = request.data.get('devices')
        #operation_hours = serializer.validated_data['operation_hours']
        
        print(facility_id,devices_data)
        devices=[]
        operation_hours=[]
        for i in devices_data:
            devices.append(i['device_id'])
            operation_hours.append(i['operation_hours'])
                
        print(devices)   
        print(operation_hours)
        
        request_data={
            "facility" : request.data.get('facility'),
            "devices" :devices,
            "operation_hours" : str(operation_hours)
        }
        serializer = EnergyAuditSerializer(data=request_data)
        if serializer.is_valid():
        
             # Calculate the energy audit result 
            audit_result = calculate_energy_audit(facility_id, devices_data, operation_hours)
            print(audit_result)
            
            serializer.save(audit_result=audit_result)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #return Response("hello")

def calculate_energy_audit(facility_id, devices_data, operation_hours):
    try:
        facility = Facility.objects.get(id=facility_id)
        devices = [device_data['device_id'] for device_data in devices_data]

        total_energy_usage = 0.0
        for device, device_data in zip(devices, devices_data):
            print(device,'heheheh')
            energy_device=EnergyDevice.objects.get(id=device)
            
            device_rating = energy_device.rating
            device_operation_hours = device_data['operation_hours']
            total_energy_usage += device_operation_hours * device_rating

        # Create the energy audit record in the database
        energy_audit = EnergyAudit.objects.create(facility=facility, operation_hours=operation_hours)
        energy_audit.devices.set(devices)
        energy_audit.audit_result = total_energy_usage
        energy_audit.save()

        return total_energy_usage

    except Facility.DoesNotExist:
        return 0.0
    
    
@api_view(['Get'])
@permission_classes([IsAuthenticated])
def get_audits(request):
    audits=EnergyAudit.objects.filter(user=request.user)
    serializer = EnergyAuditSerializer(audits, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['Get'])
@permission_classes([IsAuthenticated])
def get_devices(request):
    audits=EnergyDevice.objects.filter(user=request.user)
    serializer = EnergyDeviceSerializer(audits, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)



# # Set your OpenAI API key
# openai.api_key = "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"

# def generate_chat_prediction(prompt):
#     try:
#         response = openai.Completion.create(
#             model="gpt-3.5-turbo",
#             prompt=prompt,
#             max_tokens=50  # Adjust this based on requirements
#         )

#         # Extract the generated text from the response
#         prediction = response.choices[0].text
#         return prediction
#     except Exception as e:
#         # Handle errors
#         return str(e)


# #get prediction from gpt
# @api_view(['POST'])
# def get_chat_prediction(request):
#     if request.method == 'POST':
#         # Get the input data from the request
        
#         prompt = request.data.get('prompt', '')

#         # Generate a ChatGPT prediction
#         prediction = generate_chat_prediction(prompt)

#         return Response({'prediction': prediction}, status=200)
#     return Response({'error': 'Invalid request'}, status=400)



@api_view(['POST'])
def get_chat_prediction(request):
    if request.method == 'POST':
        email = request.data.get('yooptions@gmail.com')  # User's OpenAI email
        password = request.data.get('ch@t,Gp1')  # User's OpenAI password
        prompt = request.data.get('prompt')

        # Authenticate and obtain an access token using the user's email and password
        print('Heeeeeeeeeeeeeeer')
        response = requests.post("https://api.openai.com/v1/users/login", json={"email": email, "password": password})
        if response.status_code == 200:
            access_token = response.json()["access_token"]

            # Use the obtained access token to make a ChatGPT API request
            headers = {
                "Authorization": f"Bearer {access_token}",
                "Content-Type": "application/json"
            }

            data = {
                "prompt": prompt,
                "max_tokens": 50  # Adjust based on your requirements
            }

            chat_response = requests.post("https://api.openai.com/v1/engines/gpt-3.5-turbo/completions", headers=headers, json=data)

            if chat_response.status_code == 200:
                prediction = chat_response.json()["choices"][0]["text"]
                return Response({'prediction': prediction}, status=200)

        return Response({'error': 'Authentication failed'}, status=401)
    return Response({'error': 'Invalid request'}, status=400)
