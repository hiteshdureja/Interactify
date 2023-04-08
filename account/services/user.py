from account.models import Users, UserCredentials
from common.services.email import EmailService


class UserService:
    @staticmethod
    def create_user(first_name, last_name, dob, email, password):
        # creating entry in model
        user = Users.create_user(
            first_name=first_name, last_name=last_name, dob=dob, email=email
        )
        hashed_password = hash(password)
        # creating record in user credentials with verified =False
        UserCredentials.create_user_credentials(hashed_password=hashed_password)
        # trigger email
        EmailService.trigger(email=email)
        return user

    @staticmethod
    def validate_otp(user_id, otp):
        # validate otp from redis
        otp_from_redis = 1234
        if otp != otp_from_redis:
            return False
        UserCredentials.mark_verify(user_id=user_id)
        return True

    @staticmethod
    def user_profile():
        # get user profile
        pass

    @staticmethod
    def update_user():
        # update user profile
        pass
