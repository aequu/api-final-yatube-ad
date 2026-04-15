from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator


from posts.models import Comment, Follow, Group, Post, User


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        fields = '__all__'
        model = Comment


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    following = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username'
    )

    def validate_following(self, value):
        request = self.context.get('request')
        if request and request.user == value:
            raise serializers.ValidationError("Нельзя подписаться на самого себя.")
        return value

    class Meta:
        fields = '__all__'
        model = Follow


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = "__all__"
