import argparse
import uvicorn

from api.http_handles import app


def start_service():
    parser = argparse.ArgumentParser(description="Your application description.")
    parser.add_argument("--host", type=str, default="0.0.0.0", help="Host address")
    parser.add_argument("--port", type=int, default=8888, help="Port number")
    args = parser.parse_args()
    uvicorn.run(app=app, host=args.host, port=args.port, log_level="info")
