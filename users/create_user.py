from .models import User

def create_role(validated_data, profile_role):
        user_data= validated_data.pop('user')
        user= User.objects.create(**user_data)

        profile= profile_role.objects.create(user= user, **validated_data)
        return profile