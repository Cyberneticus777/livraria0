from dataclasses import fields
from rest_framework.serializers import ModelSerializer

from core.models import Categoria

from core.models import Editora

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"

class EditoraSerializer(ModelSerializer):
    class Meta:
        model = Editora
        fields = "__all__"