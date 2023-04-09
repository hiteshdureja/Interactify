from account.models import Users, UserCredentials
from common.services.email.email import BaseEmailService


class UserService:
    @staticmethod
    def create_user(user_id, first_name, last_name, dob, email, password):
        # creating entry in model
        user = Users.create_user(
            user_id=user_id,
            first_name=first_name,
            last_name=last_name,
            dob=dob,
            email=email,
        )
        hashed_password = hash(password)
        # creating record in user credentials with verified =False
        UserCredentials.create_user_credentials(hashed_password=hashed_password)
        # generate otp
        from account.services.user_credential import UserCredentialService
        generated_otp = UserCredentialService().generate_otp(user_id=user_id)
        # trigger email and sent otp to generate email
        BaseEmailService.trigger(to_email=email, message=None, subject=None)
        return user

    @staticmethod
    def user_profile():
        # get user profile
        pass

    @staticmethod
    def update_user():
        # update user profile
        pass

    @staticmethod
    def login_user(user_id, password):
        hashed_password = hash(password)
        user = UserCredentials.get_user_credential_by_id(user_id=user_id)
        if user and user.hashed_password == hashed_password:
            return True
        return False
