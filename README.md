# A simple book management API

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn

## Installation

- Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/Obcodelab/Simple-book-management-api.git
cd Simple-book-management-api
```

- Create a virtual environment and activate it:

```bash
python -m venv venv

# For windows
venv\Scripts\activate

# For MacOS or Linux
source venv/bin/activate
```

- Install the dependencies:

```bash
pip install -r requirements.txt
```

- Run the application:

```bash
uvicorn main:app --reload
```

## For official documentation

- FastAPI provides automatic documentation. Once you run the application, you can access the API docs at `http://127.0.0.1:8000/docs`.

## For testing

- Without deactivating the virtual environment, run the following command:

```bash
pytest test_main.py
```
