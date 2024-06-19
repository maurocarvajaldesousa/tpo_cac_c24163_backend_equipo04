from app import create_app

app = create_app()

if __name__ == '__main__':
    # Levanta el servidor de desarrollo de Flask
    app.run(debug=True)