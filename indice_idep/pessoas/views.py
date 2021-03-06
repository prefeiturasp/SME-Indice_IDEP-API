from django.db import connection
from django.shortcuts import render

# Create your views here.
from pessoas.api.serializers import UserSerializer
from pessoas.models import Servidores, ServidorUser
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.views import ObtainJSONWebToken

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_decode_handler = api_settings.JWT_DECODE_HANDLER


class LoginView(ObtainJSONWebToken):
    def post(self, request, *args, **kwargs):
        """
        Função que subscreve o Login do Django, utilizando algumas
        informações do Servidor para autenticação
        :param request: Requisição da chamada da função
        :return: Token de autenticação
        """
        response = super(LoginView, self).post(request, *args, **kwargs)
        res = response.data
        token = res.get('token')

        # token ok, get user
        if token:
            user = jwt_decode_handler(token)  # already json - don't serialize
        else:
            req = request.data
            rf = req.get('rf')
            password = req.get('cpf')
            anonasc = req.get('anonasc')
            mesnasc = req.get('mesnasc')

            if rf is None or password is None or anonasc is None or mesnasc is None:
                return Response({'success': False,
                                 'message': 'Missing or incorrect credentials',
                                 'data': req},
                                status=status.HTTP_400_BAD_REQUEST)

            # email exists in request, try to find user
            try:
                servidor = ServidorUser.objects.get(rf=int(rf), password=password, ano_nasc=int(anonasc),
                                                    mes_nasc=int(mesnasc))
            except:
                return Response({'success': False,
                                 'message': 'User not found',
                                 'data': req},
                                status=status.HTTP_404_NOT_FOUND)

            payload = jwt_payload_handler(servidor)
            token = jwt_encode_handler(payload)
            user = UserSerializer(servidor).data

        return Response({'success': True,
                         'message': 'Successfully logged in',
                         'token': token,
                         'user': user},
                        status=status.HTTP_200_OK)


class EscolasDoServidor(APIView):

    def get(self, request, rf, format=None):
        """
        Função que retorna um JSON com todas as escolas de um determinado Servidor
        :param request: Requisição da chamada da função
        :param rf: Parametro da url com o RF do Servidor
        :return: JSON com as escolas que trabalham o Servidor
        """
        if not rf:
            return Response('RF não informado')

        query = """        
            select distinct serv.cd_unidade_educacao_atual, escolas.tipoesc, escolas.nomesc
            from pessoas_servidores as serv
            inner join escolas_escolas as escolas on escolas.codesc = serv.cd_unidade_educacao_atual::text
            where cd_unidade_educacao_atual notnull
            and rf={};
            """.format(rf)

        cursor = connection.cursor()
        cursor.execute(query)
        modalidades = {'results':
                           [dict(zip([column[0] for column in cursor.description], row))
                            for row in cursor.fetchall()]}

        return Response(modalidades)
