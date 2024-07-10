# Prestige Urbane

![alt text](prestige_urbane\static\images\PrestigeUrbane.png)

## Introduction

Prestige Urbane is a web application designed to elevate your fashion shopping experience. Our platform allows users to browse and select from a curated collection of contemporary urban clothing, ensuring a seamless and stylish shopping journey.

## Authors
Soufiane El Houmy - [Github](https://github.com/SoufianeElHoumy) / [Twitter](https://twitter.com/ElHoumySoufiane)   / [linkedin](https://www.linkedin.com/in/soufiane-el-houmy-2692a6288/)

Oussama EL GUENNOUNI - [Github](https://github.com/Ousskira) / [Twitter](https://twitter.com/OussamaELG2709)   / [linkedin](https://www.linkedin.com/in/oussama-el-guennouniouni-5657461b6)

Reda Adjar - [Github](https://github.com/MrBoodj011) / [Twitter](https://x.com/adjar_reda5)   / [linkedin](https://www.linkedin.com/in/redaadjar/)

## Installation

To run this project locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/SoufianeElHoumy/prestige_urbane.git
    cd prestige_urbane
    ```

2. Create a virtual environment:
    ```bash
    cd prestige_urbane
    python -m venv env
    source env/bin/activate   # On Windows, use `env\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    pip install django
    ```

4. Configure your SQLite database in `settings.py`:

    ```python
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
    }
    ```

5. Apply migrations:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6. Run the development server:
    ```bash
    python manage.py runserver
    ```

7. Open your browser and navigate to `http://127.0.0.1:8000/`.

## Usage

1. Register for an account or log in if you already have one.
2. Browse the available products.
3. Add desired products to your cart.
4. Proceed to checkout to place your order for pickup at the grocery store.

## Contributing

We welcome contributions to the Prestige Urbane project. To contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch:
    ```bash
    git checkout -b feature-name
    ```
3. Make your changes and commit them with descriptive messages:
    ```bash
    git commit -m "Description of the feature"
    ```
4. Push your changes to your forked repository:
    ```bash
    git push origin feature-name
    ```
5. Open a pull request with a detailed description of your changes.

## Related Projects

- [Prestige Urbane Landing Page](https://github.com/SoufianeElHoumy/Prestige_Urban_LandingPage)

## Prestige Urbane Logo
![Prestige Urbane Logo](static/images/1.png)