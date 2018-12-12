from django.contrib.auth import update_session_auth_hash

from rest_framework import serializers

from authentication.models import Account

class AccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)
    confirm_password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Account
        fields = ('id','email','username','first_name','last_name',
                  'team_name','city','state','acct_type','created_at',
                  'updated_at', 'password', 'confirm_password')
        read_only_fields = ('username', 'created_at', 'updated_at')

        def create(self, validated_data):
            print type(validated_data)
            return Account.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.email = validated_data.get('email', instance.email)
            instance.first_name = validated_data.get('first_name', instance.first_name)
            instance.last_name = validated_data.get('last_name', instance.last_name)
            instance.team_name = validated_data.get('team_name', instance.team_name)
            instance.city = validated_data.get('city', instance.city)
            instance.state = validated_data.get('state', instance.state)
            instance.acct_type = validated_data.get('acct_type', instance.acct_type)

            instance.save()

            #TODO: naive implementation?
            password = validated_data.get('password', None)
            confirm_password = validated_data.get('confirm_password', None)

            if password and confirm_password and password == confirm_password:
                instance.set_password(password)
                instance.save()

            update_session_auth_hash(self.context.get('request'), instance)

            return instance
