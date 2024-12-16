from rest_framework.decorators import api_view
from rest_framework.response import Response

from comments.models import Comments
from comments.serializers import CommentsSerializer

@api_view(['GET', 'POST'])
def get_post_comments(request):
    """
    Представление для получения списка всех/ограниченого числа комментариев
    или публикации нового.
    """

    if request.method == 'GET':
        car_id = request.GET.get('car_id')
        limit = request.GET.get('limit', 'all')
        comments = Comments.objects.filter(car_id=car_id).order_by('-comment_date')
        if limit != 'all':
            comments = comments[:limit]
        serializer = CommentsSerializer(comments, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        car_id = request.POST.get('car_id')
        comment = request.POST.get('comment')
        client_name = request.POST.get('client_name', 'Аноним')
        new_comment = Comments.objects.create(car_id=car_id, comment=comment, client_name=client_name)
