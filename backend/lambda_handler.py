from mangum import Mangum
from server import app

# Create lambda handler 
handler = Mangum(app)