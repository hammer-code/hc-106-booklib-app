from dotenv import load_dotenv
load_dotenv()

from booklib.app import create_app

app = create_app()

if __name__ == 'main':
  app.run(host='0.0.0.0', port='6000')
