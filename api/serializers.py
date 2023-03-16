from rest_framework.serializers import ModelSerializer
from .models import Note

class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        # serialize all attributeds in this model+
        fields = '__all__' #could be a list of attributes