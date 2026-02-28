from app import create_app
import os

app = create_app()

if __name__ == '__main__':
    port = app.config.get('PORT', 5000)
    debug = app.config.get('DEBUG', True)
    app.run(debug=debug, port=port)
