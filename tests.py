import time

from logger import LoggingELK

logging = LoggingELK(insert_elk=True, elk_host="https://search-elk-prd-o2zsrgd73h7gg57zqcuf4c55he.us-east-1.es.amazonaws.com/")

while True:
    time.sleep(5)
    logging.info("simulando uma info")
    logging.error("simulando um erro")
    logging.warning("simulando um warning")

# python3 setup.py sdist bdist_wheel
# python3 -m twine upload --repository pypi dist/*
