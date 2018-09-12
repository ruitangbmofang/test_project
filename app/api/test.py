from app import create_app
import json

app = create_app()
app_ctx = app.app_context()
app_ctx.push()

test_app = app.test_client()


def test_goods():
    response = test_app.post('/goods/addgoods/', data=json.dumps({"name": "test", "num": "2", "unit_price": "1.58"}), content_type='application/json')
    print response.status_code


test_goods()

"""
2 自定义验证器 - namefield验证器

在类里面，编写 def validate_namefieldxxx(form, field)函数，通过raise ValidationError提示错误信息，编写在类里面的验证器，不需要在显示在feild里面指定validators=， 比如

class LoginForm(Form):

    openid = StringField('openid', validators=[DataRequired()])

    remember_me = BooleanField('remember_me', default=False)

    def validate_remember_me(form, field):

        if field.data != False:

            raise ValidationError('remember_me must be False')

 

3 自定义验证器 - 把验证器编写成单独的函数

这样需要在feild里面指定validators=，比如

def validate_remember_me(form, field):

    if field.data != False:

        raise ValidationError('remember_me must be False2')

      

class LoginForm(Form):

    openid = StringField('openid', validators=[DataRequired()])

    remember_me = BooleanField('remember_me', default=False,

                               validators=[validate_remember_me ])

 

4 自定义验证器 - 把验证器编写成单独的类

class Length(object):

    def __init__(self, min=-1, max=-1, message=None):

        self.min = min

        self.max = max

        if not message:

            message = u'Field must be between %i and %icharacters long.' % (min, max)

        self.message = message

 

    def __call__(self, form, field):

        l = field.data and len(field.data) or 0

        if l < self.min or self.max != -1 and l > self.max:

            raise ValidationError(self.message)

 

length = Length

 

class MyForm(Form):

    name = StringField('Name', [InputRequired(), length(max=50)])
"""