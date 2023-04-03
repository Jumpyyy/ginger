"""
    Created by ldd on 2023/3/29 19:02
"""
from app.app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)