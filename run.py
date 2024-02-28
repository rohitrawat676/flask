from flask_task import create_app
from flask_sqlalchemy import SQLAlchemy


app = create_app()

db = SQLAlchemy(app)

if __name__ == '__main__':

    # db.init_app(app)
    app.run(debug=True)
