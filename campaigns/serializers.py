from django.contrib.auth import get_user_model
from enumfields.drf.serializers import EnumSupportSerializerMixin
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import (
    ModelSerializer
)

from campaigns.models import Campaign, CampaignPartyRelation
from csecourses.models import CSECourseGroup
from csecourses.serializers import CSECourseGroupTermSerializer
from users.serializers import ProfileRetrieveSerializer

User = get_user_model()


class CampaignAsCourseSerializer(EnumSupportSerializerMixin, ModelSerializer):
    title = SerializerMethodField()

    class Meta:
        model = Campaign
        fields = [
            'id',
            'title',
            'graders'
        ]

    def get_title(self, obj: Campaign):
        return obj.name


class CampaignAsCourseSimpleSerializer(EnumSupportSerializerMixin, ModelSerializer):
    title = SerializerMethodField()
    group = SerializerMethodField()
    multi_group = SerializerMethodField()

    class Meta:
        model = Campaign
        fields = [
            'id',
            'title',
            'group',
            'multi_group'
        ]

    def get_title(self, obj: Campaign):
        return obj.name

    def get_group(self, obj: Campaign):
        if obj.course_data:
            return obj.course_data.course_group.group
        else:
            return None

    def get_multi_group(self, obj: Campaign):
        if obj.course_data:
            return CSECourseGroup.objects.filter(
                course=obj.course_data.course_group.course
            ).count() > 1
        else:
            return None


class GraderRelationSerializer(EnumSupportSerializerMixin, ModelSerializer):
    campaign = CampaignAsCourseSimpleSerializer()
    content_object = ProfileRetrieveSerializer()
    class Meta:
        model = CampaignPartyRelation
        fields = [
            'campaign',
            'content_object',
            'status'
        ]

class CampaignGraderyRequestSerializer(EnumSupportSerializerMixin, ModelSerializer):
    class Meta:
        model = CampaignPartyRelation
        fields = [
            'id',
            'enrollment_request_note'
        ]