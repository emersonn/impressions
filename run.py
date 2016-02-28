from impressions import app
from impressions import db

db._create_all()
app.run()
