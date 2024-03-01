from flask_task import create_app
# from flask_sqlalchemy import SQLAlchemy


app = create_app()

# db = SQLAlchemy(app)


if __name__ == '__main__':

    # db.init_app(app)

    enviroment = input("Enter the enviroment: ")
    try:
        enviroment = enviroment
    except ValueError:
        print("Invalid Input please give input as dev or stage.")

    if enviroment == "stage":
        app.run(host=app.config['STAGE_HOSTNAME'],
                port=app.config['STAGE_PORT'])
    elif enviroment == "dev":
        app.run(host=app.config['DEV_HOSTNAME'], port=app.config['DEV_PORT'])
    else:
        app.run(debug=True, host='127.0.0.1', port=5000)
