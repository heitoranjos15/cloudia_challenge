import os
from app import create_app
from config import configs

env = configs.get(os.environ.get('service_env', 'dev'))

app = create_app(env)
app.run(debug=True)