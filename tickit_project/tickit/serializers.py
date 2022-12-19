from rest_framework import serializers
from .models import Venue, Event

class VenueSerializer(serializers.HyperlinkedModelSerializer):
    event = serializers.HyperlinkedRelatedField(
        view_name='event_detail',
        many=True,
        read_only=True
    )
    venue_url = serializers.ModelSerializer.serializer_url_field(
        view_name = 'venue_detail'
    )
    class Meta:
        model = Venue
        fields = ('id','name', 'event', 'address','onsite_parking','capacity','venue_url','photo_url','description')

class EventSerializer(serializers.HyperlinkedModelSerializer):
    venue = serializers.HyperlinkedRelatedField(
        view_name='venue_detail',
        read_only=True
    )
    event_url = serializers.ModelSerializer.serializer_url_field(
        view_name = 'event_detail'
    )
    venue_id = serializers.PrimaryKeyRelatedField(
        queryset=Venue.objects.all(),
        source= 'venue'
    )

    class Meta:
        model = Event
        fields = ('id', 'venue', 'venue_id', 'name', 'type', 'description','ASL_interpreter','alcohol_served','event_url','photo_url')