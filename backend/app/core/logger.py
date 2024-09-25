import logging

logging.basicConfig(
    level=logging.DEBUG,  # Change this to INFO or ERROR in production
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)


def get_logger(name: str | None = None) -> logging.Logger:
    if name:
        return logging.getLogger(name=name)
    return logging.getLogger("ROOT")
