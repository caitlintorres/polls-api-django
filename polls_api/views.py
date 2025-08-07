from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Poll, Option
from .serializers import PollSerializer, OptionSerializer

class PollListCreate(APIView):
    def get(self, request):
        polls = Poll.objects.all()
        serializer = PollSerializer(polls, many=True)
        return Response(serializer.data)

    def post(self, request):
        options_data = request.data.pop("options", [])
        poll = Poll.objects.create(**request.data)
        for option in options_data:
            Option.objects.create(poll=poll, **option)
        serializer = PollSerializer(poll)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class PollDetail(APIView):
    def get(self, request, pk):
        try:
            poll = Poll.objects.get(pk=pk)
        except Poll.DoesNotExist:
            return Response({"error": "Not found"}, status=404)
        serializer = PollSerializer(poll)
        return Response(serializer.data)

    def delete(self, request, pk):
        try:
            poll = Poll.objects.get(pk=pk)
        except Poll.DoesNotExist:
            return Response({"error": "Not found"}, status=404)
        poll.delete()
        return Response(status=204)

class VoteView(APIView):
    def post(self, request, pk):
        option_id = request.query_params.get("option_id")
        try:
            option = Option.objects.get(pk=option_id, poll_id=pk)
        except Option.DoesNotExist:
            return Response({"error": "Option not found"}, status=404)
        option.votes += 1
        option.save()
        return Response({"message": "Vote recorded"})
