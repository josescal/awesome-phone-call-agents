import logging

from quotewake_salesforce.structured_logging import log_event


def test_structured_events_redact_phone_and_secret_values(caplog):
    logger = logging.getLogger("quotewake_salesforce")
    logger.addHandler(caplog.handler)
    logger.setLevel(logging.INFO)
    try:
        log_event("safe_event", phone="+34910000001", api_key="super-secret")
    finally:
        logger.removeHandler(caplog.handler)
    rendered = repr([getattr(record, "quotewake_fields", {}) for record in caplog.records])
    assert "+34910000001" not in rendered
    assert "super-secret" not in rendered
