#! /bin/env python
import uvicorn
from apps.admin_app import app as admin_app
from apps.message_app import app as message_app


if __name__ == "__main__":
    uvicorn.run(admin_app, host="0.0.0.0", port=8000)
