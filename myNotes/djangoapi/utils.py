from .models import Note
from .serializers import NoteSerializer
from rest_framework.response import Response

def getNoteUtil(request):
    notes=Note.objects.all().order_by('-updated')
    serializer=NoteSerializer(notes,many=True)
    return Response(serializer.data)

def createNoteUtil(request):
    data=request.data
    notes=Note.objects.create(body=data['body'])
    serializer=NoteSerializer(notes,many=False)
    return Response(serializer.data)

def getNoteDetailsUtil(request,pk):
    notes=Note.objects.get(id=pk)
    serializer=NoteSerializer(notes,many=False)
    return Response(serializer.data)

def updateNoteUtil(request,pk):
    data=request.data
    notes=Note.objects.get(id=pk)
    serializer=NoteSerializer(instance=notes,data=data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

def deleteNoteUtil(request,pk):
    notes=Note.objects.get(id=pk)
    notes.delete()
    return Response("Note is deleted")


