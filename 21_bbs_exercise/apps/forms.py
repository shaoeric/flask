from flask_wtf import Form

class BaseForm(Form):
    def get_error(self):
        message = self.errors.popitem()[0][1]
        return message