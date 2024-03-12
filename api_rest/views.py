from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import UserSerializer

'''
def data_base_em_django():

    # Busca um usuario especifico através do pk (primary key)
    data = User.objects.get(pk='vermelho') # Retorna um objeto

    # Busca todos os usuarios que possuem a idade 20, realiza um filtro
    data = User.objects.filter(user_age=20) # Retorna um QuerySet

    # Busca todos os usuarios que não possuem a idade 20, realiza um filtro
    data = User.objects.exclude(user_age=20) # Retorna um QuerySet

    # QuerySet é uma lista de objetos, logo, podemos iterar sobre ele

    data.save() # Salva o objeto no banco de dados

    data.delete() # Deleta o objeto do banco de dados
'''

# Create your views here.

@api_view(['GET'])
def get_users(request):
     
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_user(requet, pk):

    if requet.method == 'GET':
        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def user_manager(request):

    if request.method == 'GET':
        try:
            if request.GET['user']: # user é um pamaetro que vem na url (ex: /user_manager?user=vermelho)

                user_nickname = request.GET['user']

                user = User.objects.get(pk=user_nickname)
                serializer = UserSerializer(user)
                return Response(serializer.data, status=status.HTTP_200_OK)
            
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'POST':
        
        data = request.data
        serializer = UserSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PUT':

        try:
            nickname = request.data['user_nickname']

            old_user = User.objects.get(pk=nickname)

            serializer = UserSerializer(old_user, data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        
        nickname = request.GET['user']
        try:
            user_to_delete = User.objects.get(pk=nickname)
            print(user_to_delete)
            user_to_delete.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)




