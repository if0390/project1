import logging
import logging.config
import os

def setup_logging(default_path='logging.conf', default_level=logging.INFO):
    """Set up logging configuration."""
    if os.path.exists(default_path):
        logging.config.fileConfig(default_path)
    else:
        logging.basicConfig(level=default_level)

def main():
    setup_logging() 
    logging.info("Application started.") 
    try:
        from app.repl import REPL
        repl = REPL()
        repl.start()
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        logging.info("Application exited.")

if __name__ == "__main__":
    main()