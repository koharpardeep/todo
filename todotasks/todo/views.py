from rest_framework.response import Response
from rest_framework.views import APIView
from .models import TodoDetails
from .serializers import TodoSerializer
from django.http import HttpResponse
from django.core import serializers


class CreateTodo(APIView):

    def post(self, request):
        try:
            _data = request.POST
            state = _data.get('state')
            due_date = _data.get('due_date')
            text = _data.get('text')

            todoserializer = TodoSerializer(data=request.POST)
            if todoserializer.is_valid(raise_exception=True):
                TodoDetails.objects.create(state=state, due_date=due_date, text=text)
                return Response({'code': 200, 'message': "success"})
        except Exception as e:
            return Response({'code': 400, 'message': str(e)})


class GetAllTodos(APIView):

    def get(self,request):
        try:
            orderby = request.GET.get('orderby')
            if orderby not in ['state', 'due_date', 'both']:
                return Response({'code': 400, 'message': "filter options are ['state', 'due_date', 'both']"})
            if orderby == 'state':
                ob = 'state'
            elif orderby == 'due_date':
                ob = 'due_date'
            else:
                ob = 'both'
            if not ob == 'both':
                data = TodoSerializer(TodoDetails.objects.order_by(ob), many=True).data
            else:
                data = TodoSerializer(TodoDetails.objects.order_by('state','due_date'), many=True).data
            MAPPING_LIST = ['todo', 'in_progress', 'done']
            for each in data:
                each['state'] = MAPPING_LIST[each['state']]
            return Response({'code': 200, 'data': data, 'message': 'success'})
        except Exception as e:
            return Response({'code': 400, 'message': str(e)})

class Updatetodo(APIView):

    def post(self,request):
        try:
            _data = request.POST
            todo_id = _data.get('id')
            state = _data.get('state')
            due_date = _data.get('due_date')
            text = _data.get('text')

            todoserializer = TodoSerializer(data=request.POST)
            if todoserializer.is_valid(raise_exception=True):
                TodoDetails.objects.filter(id=todo_id).update(state=state, due_date=due_date, text=text)
                return Response({'code': 200, 'message': "success"})
        except Exception as e:
            return Response({'code': 400, 'message': str(e)})


class DeleteTodo(APIView):
        def post(self, request):
            try:
                _data = request.POST
                todo_id = _data.get('id')
                if todo_id is None:
                    return Response({'code': 400, 'message': 'Todo Id is required'})
                TodoDetails.objects.get(id=todo_id).delete()
                return Response({'code': 200, 'message': 'success'})
            except Exception as e:
                return Response({'code': 400, 'message': str(e)})