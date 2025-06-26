from .models import User

# def create_role(validated_data, profile_role):
#         user_data= validated_data.pop('user')
#         password= validated_data.pop('password', None)
#         user= User.objects.create(password= password,**user_data)

#         profile= profile_role.objects.create(user= user, **validated_data)
#         return profile

def create_role(validated_data, role_model):
    user_data = validated_data.pop('user')
    password = user_data.pop('password', None)  

    user = User.objects.create_user(**user_data, password=password)

    role = role_model.objects.create(user=user, **validated_data)
    return role