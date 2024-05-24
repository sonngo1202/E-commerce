import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Comment
from .serializers import CommentSerializer, CommentShowSerializer

class AddCommentView(APIView):
    def post(self, request):
        serializer = CommentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ListCommentOfProduct(APIView):
    def get(self, request):
        type = request.data.get('type')
        product_id = request.data.get('product_id')
        comments = Comment.objects.filter(type=type, product_id=product_id)
        data = []
        for comment in comments:
            user = self.get_user_info(comment.user_id)
            fullname = user.get('fullname', {})
            item = {
                'id': comment.id,
                'coomment': comment.comment,
                'rate': comment.rate,
                'date_added': comment.date_added,
                'user_full_name': f"{fullname.get('first_name', '')} {fullname.get('last_name', '')}"
                
            }
            data.append(item)
        return Response(data, status=status.HTTP_200_OK)
    
    def get_user_info(self, user_id):
        url = f"http://localhost:8001/api/ecomSys/user/info/user_id={user_id}"
        response = requests.get(url)
        return response.json()