# Primeiro, importe o modelo Comment.
from .models import Comment
# Importe o módulo forms do Django.
from django import forms

# Agora, defina a classe CommentForm.
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment  # Especifica que o modelo para o formulário é Comment.
        fields = ("name", "email", "body")  # Especifica os campos a serem incluídos no formulário.
