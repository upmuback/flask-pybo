from pybo import create_app
import sys

app = create_app()

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port = int(sys.argv[1]))
    
    