import sys
import os.path
import configparser

import pytest
from faker import Faker


@pytest.fixture
def faker():
    return Faker()


def pytest_addoption(parser):
    parser.addoption(
        "--env", action="store", default="local", help="env variable name"
    )


# def read_ini():
#     config_file_name = os.environ.get("config-file", "project-config.ini")
#     root_path = os.path.join(sys.path[0], config_file_name)
#     parser = configparser.ConfigParser()
#     parser.read(root_path)
#     return parser


# def get_config(request):
#     env_name = request.config.getoption('--env')
#     try:
#         return read_ini()[env_name]
#     except KeyError:
#         raise Exception(f"Wrong configuration [{env_name}]")


# @pytest.fixture(scope="session")
# def config(request):
#     config = get_config(request)
#     return config


