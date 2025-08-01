""" Event logging for application """
import logging as LOG

LOG.basicConfig(                                    #can only call basicConfig once
    format="{asctime} - {levelname} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M",
    level=LOG.DEBUG,
    filename="app.log",
    encoding="utf-8",
    filemode="a",
)
