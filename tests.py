import time

from logger import LoggingELK

logging = LoggingELK(insert_elk=True, elk_host="")

while True:
    time.sleep(5)
    logging.info("simulando uma info")
    logging.error("simulando um erro")
    logging.warning("simulando um warning")

# python3 setup.py sdist bdist_wheel
# python3 -m twine upload --repository pypi dist/*
