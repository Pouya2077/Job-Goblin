import logging
from event_logging import LOG

def test_event_logger(caplog):
    levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
    LOG.handlers = []
    LOG.propagate = True

    with caplog.at_level(logging.DEBUG):
        LOG.debug("TEST debug msg.")
        LOG.info("TEST info msg.")
        LOG.warning("TEST warning msg.")
        LOG.error("TEST error msg.")
        LOG.critical("TEST critical msg.")

    for level in levels:
        level = level.lower()
        assert f"TEST {level} msg." in caplog.text

    for level in levels:
        assert any(record.levelname == level for record in caplog.records)
