Logging is the "black box" flight recorder for your code. While `print()` tells you what’s happening *now*, `logging` tells you what happened at 3:00 AM when the server crashed while you were sleeping.

---

## 🟢 Level 1: The Beginner (Severities & Basic Config)

The first rule of professional Python: **Stop using `print()` for debugging.** `print()` is hard to turn off, hard to search, and provides no context.

### The 5 Standard Levels

| Level | Value | Use Case |
| --- | --- | --- |
| **DEBUG** | 10 | Detailed info, typically of interest only when diagnosing problems. |
| **INFO** | 20 | Confirmation that things are working as expected. |
| **WARNING** | 30 | Something unexpected happened, but the app is still working. |
| **ERROR** | 40 | Due to a more serious problem, the software has not been able to perform some function. |
| **CRITICAL** | 50 | A serious error, indicating that the program itself may be unable to continue running. |

### Simple Setup

```python
import logging

# Basic configuration
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='app.log', # Saves to a file
    filemode='a'         # 'a' for append, 'w' for overwrite
)

logging.info("Application started")
logging.error("Failed to connect to database")

```

---

## 🟡 Level 2: The Intermediate (Handlers & Formatters)

In real apps, you don't just want one log file. You want logs to go to the **Console** (for development) and a **File** (for production).

### Creating a Custom Logger

Instead of the "root" logger, we use `__name__`. This tells you exactly which file generated the log.

```python
import logging

# 1. Create a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# 2. Create Handlers (Where the logs go)
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler('error.log')
file_handler.setLevel(logging.ERROR) # Only save Errors to the file

# 3. Create a Formatter (What the logs look like)
formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# 4. Add Handlers to the Logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

logger.info("This goes to console.")
logger.error("This goes to BOTH console and file.")

```

---

## 🔴 Level 3: The Advanced (Production Grade)

For large apps, we use `dictConfig`. This allows you to define your entire logging strategy in a dictionary (or JSON/YAML file).

### Key Advanced Features:

* **Rotating Files:** Prevents log files from becoming 50GB and crashing your server.
* **JSON Logging:** Makes logs "machine-readable" for tools like ELK or Datadog.
* **Tracebacks:** Capturing the full error stack automatically.

```python
import logging.config

LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'},
        'json': {'class': 'pythonjsonlogger.jsonlogger.JsonFormatter'}
    },
    'handlers': {
        'default': {
            'level': 'INFO',
            'formatter': 'standard',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'app.log',
            'maxBytes': 10485760, # 10MB
            'backupCount': 5
        },
    },
    'loggers': {
        '': {'handlers': ['default'], 'level': 'DEBUG', 'propagate': True}
    }
}

logging.config.dictConfig(LOGGING_CONFIG)

```

---

## 🚀 Field-Specific Applications

### 1. Web Apps (Flask/FastAPI)

**Use Case:** Tracking a single user request across multiple functions.

* **Tip:** Inject a `request_id` into every log so you can filter all logs for one specific failed transaction.

```python
@app.middleware("http")
async def log_requests(request: Request, call_next):
    request_id = str(uuid.uuid4())
    logger.info(f"Request {request_id} started: {request.url.path}")
    response = await call_next(request)
    logger.info(f"Request {request_id} finished")
    return response

```

### 2. AI Apps (Training/Mance)

**Use Case:** Auditing model decisions and resource usage.

* **Tip:** Log the **Model Version**, **Input features**, and **Prediction Confidence**. This is vital for "Explainable AI."

```python
def predict(data):
    logger.info("Inference started", extra={
        "model_version": "v2.1",
        "input_shape": data.shape
    })
    prediction = model.predict(data)
    logger.info(f"Prediction made: {prediction}", extra={"confidence": 0.98})
    return prediction

```

### 3. Computer Vision Apps (OpenCV/PyTorch)

**Use Case:** Performance monitoring and metadata tracking.

* **Tip:** Log the **FPS (Frames Per Second)** and the number of objects detected per frame.

```python
import time

def process_frame(frame):
    start_time = time.time()
    # ... detection logic ...
    fps = 1.0 / (time.time() - start_time)
    
    if fps < 20:
        logger.warning(f"Performance Drop! FPS: {fps:.2f}")
    
    logger.debug(f"Detected {len(objects)} objects in frame.")

```

---

## ✅ Best Practices for 2025

1. **Never log secrets:** Use filters to strip out passwords or API keys before they hit the file.
2. **Use `logger.exception()`:** Inside an `except` block, use `logger.exception("message")`. It automatically attaches the full stack trace.
3. **Lazy Formatting:** Use `logger.info("User %s", name)` instead of f-strings `f"User {name}"`. This is faster because Python won't format the string if the log level is disabled.
4. **Consider `Loguru`:** If you want a modern, "zero-config" experience, the `loguru` library is the gold standard in 2025.

