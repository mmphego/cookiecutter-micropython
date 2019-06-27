from {{ cookiecutter.project_slug }} import {{ cookiecutter.project_slug }}
from utils import read_config

if __name__ == "__main__":
    filename = "config.json"
    config = read_config(filename)
    # Code goes here