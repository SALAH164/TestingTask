import re
from typing import Optional


class UserValidation:    
    @staticmethod
    def validate_email(email: Optional[str]) -> bool:

        if email is None or email == "": return False
        
        emailRegex = r'^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$'
        
        return re.match(emailRegex, email) is not None
    
    @staticmethod
    def validate_username(username: Optional[str]) -> bool:

        if username is None or username == "": return False
        
        usernameRegex = r'^[a-zA-Z0-9_]{3,20}$'
        
        return re.match(usernameRegex, username) is not None
    
    @staticmethod
    def validate_phone_number(phone: Optional[str]) -> bool:

        if phone is None or phone == "": return False
        
        localNumberRegex = r'^(010|011|012|015)\d{8}$'
        
        return re.match(localNumberRegex, phone) is not None
    
    @staticmethod
    def validate_national_id(national_id: Optional[str]) -> bool:

        if national_id is None or national_id == "":
            return False
        
        if not re.match(r'^\d{14}$', national_id):
            return False
        
        century = national_id[0]
        year = national_id[1:3]
        month = national_id[3:5]
        day = national_id[5:7]
        governorate = national_id[7:9]
        
        if century not in ['2', '3']:
            return False
        
        month_int = int(month)
        if month_int < 1 or month_int > 12:
            return False
        
        day_int = int(day)
        if day_int < 1 or day_int > 31:
            return False
        
        governorate_int = int(governorate)
        if governorate_int < 1 or governorate_int > 88:
            return False
        
        return True
