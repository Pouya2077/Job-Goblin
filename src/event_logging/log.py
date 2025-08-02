""" Event logging for application """
import logging

LOG = logging.getLogger("job_goblin")
LOG.setLevel(logging.DEBUG)
LOG.propogate = False       #avoid root logger

file_handler = logging.FileHandler("app.log", encoding="utf-8", mode="a")
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    fmt="{asctime} - {levelname} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M",
)

file_handler.setFormatter(formatter)
LOG.addHandler(file_handler)
