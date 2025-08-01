""" Event logging for application """
import logging as log

log.basicConfig(level=log.DEBUG)
log.basicConfig(
    format="{asctime} - {levelname} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M",
)

log.debug("Test debug message.")
log.warning("Test wanring message.")
