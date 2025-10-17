from flask import Flask, Response
from prometheus_client import start_http_server, Counter, generate_latest
import random
import time
import threading

app = Flask(__name__)

# Define custom Prometheus Counter metric
REQUEST_COUNT = Counter(
    'http_requests_total', 
    'Total number of requests made to the application',
    ['method', 'endpoint']
)

@app.route('/')
def home():
    # Increment the metric when this endpoint is hit
    REQUEST_COUNT.labels(method='GET', endpoint='/').inc()
    time.sleep(random.uniform(0.1, 0.5))  # Simulate processing time
    return 'Backend V1: Data processed successfully! Metrics updated.'

@app.route('/metrics')
def metrics():
    """Endpoint for Prometheus to scrape application metrics."""
    return Response(generate_latest(), mimetype='text/plain; version=0.0.4; charset=utf-8')

def start_metrics_server():
    """Starts a separate HTTP server for Prometheus scraping on port 8000."""
    start_http_server(8000)

if __name__ == '__main__':
    # Start the metrics server in a separate thread
    threading.Thread(target=start_metrics_server).start()
    
    # Start the main Flask application
    app.run(host='0.0.0.0', port=5000)