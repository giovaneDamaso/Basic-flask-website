#import from the aplication created to run
from website import create_app

app = create_app()

#run the website not the webserver
if __name__ == '__main__':
    #with every change made rerun the server
    app.run(debug=True, host='0.0.0.0')