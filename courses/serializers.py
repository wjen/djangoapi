from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import Course, Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'name', 'language', 'price', 'url')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    # snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
    # use below if using hyperlinked instead of modelserializer
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'email', 'groups', 'username', 'snippets']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
        
class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    # Because we've included format suffixed URLs such as '.json', we also need to indicate on the highlight field that any format suffixed hyperlinks it returns should use the '.html' suffix.
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ['url', 'id', 'highlight', 'owner',
                'title', 'code', 'linenos', 'language', 'style']