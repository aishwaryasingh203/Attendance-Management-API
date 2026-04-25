import bcrypt

class Hash:
    @staticmethod
    def bcrypt(password: str):
        # 1. Truncate to 72 bytes to satisfy bcrypt limits
        safe_password = password[:72]
        # 2. Encode to bytes, hash it, and decode back to string for storage
        return bcrypt.hashpw(safe_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    @staticmethod
    def verify(plain_password, hashed_password):
        # 1. Truncate input for verification
        safe_password = plain_password[:72]
        # 2. Check password
        return bcrypt.checkpw(safe_password.encode('utf-8'), hashed_password.encode('utf-8'))