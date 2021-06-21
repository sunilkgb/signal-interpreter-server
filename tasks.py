import os 
from subprocess import call
from invoke import task

CURR_DIR = os.path.abspath(os.path.dirname(__file__))
SRC_DIR = os.path.join(CURR_DIR, "source")
TEST_DIR = os.path.join(CURR_DIR, "test")
COV_PATH = os.path.join(CURR_DIR, ".coveragerc")

@task
def style(_):
    call(f"pycodestyle {SRC_DIR} --ignore=E501", shell=True)

@task
def lint(_):
    call(f"pylint {SRC_DIR}", shell=True)

@task
def test(_):
    cmd = f"pytest {TEST_DIR} --cov {SRC_DIR} --cov-config={COV_PATH}"
    call(cmd, shell=True)