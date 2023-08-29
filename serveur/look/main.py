from app import db, migrate
from migrate import *
from api import *

app.run(host="0.0.0.0", port=8887)