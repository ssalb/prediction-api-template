import os

API_VERSION = 1

DB_HOST = os.environ["REDIS_HOST"]
DB_PORT = 6379
DB_ID = 0

DB_QUEUE = "default_queue"
BATCH_SIZE = 16
SERVER_SLEEP = 0.25
CLIENT_SLEEP = 0.25
