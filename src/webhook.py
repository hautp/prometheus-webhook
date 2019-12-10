#/usr/bin/env python
from app import app 
from funcs.setup_logging import logger


if __name__ == '__main__':
    app.run(debug=False)