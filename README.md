# Two-Tier Dockerized App with Host and Application Monitoring

## Developed by: Anish Kumar

This project is a functional demonstration of core **DevOps and Cloud Monitoring** skills. It involves deploying a complete microservice stack and a robust observability platform onto a single **AWS EC2** instance.

### Project Goal
To establish end-to-end monitoring for a containerized application and its host infrastructure using open-source tools.

---

### Technology Stack

| Category | Tool | Function in Project |
| :--- | :--- | :--- |
| **Cloud/Host** | **AWS EC2 (T3.micro)** | Free Tier compliant hosting (Asia Pacific - Mumbai region). |
| **Containerization** | **Docker / Docker Compose** | Used to define, build, and run the entire 5-container multi-service stack. |
| **Application** | **Python Flask / Nginx** | Two-tier application providing backend logic and frontend display. |
| **Metrics Collection** | **Prometheus** | Scrapes host metrics (`localhost:9100`) and application metrics (`backend:8000`). |
| **Visualization** | **Grafana** | Used to visualize the collected data via the Node Exporter dashboard and custom PromQL queries. |

---

### Deployment & Validation Summary

1.  **Deployment Method:** Deployed using `docker compose up -d`.
2.  **Infrastructure Monitoring:** Verified that the **Node Exporter** target is **UP** in Prometheus and populates the host performance dashboard in Grafana.
3.  **Application Monitoring:** The Python backend is **instrumented** to track `http_requests_total`, which is scraped by Prometheus.
4.  **Access:**
    * **Application Frontend:** `http://<EC2_PUBLIC_IP>:80`
    * **Grafana Dashboard:** `http://<EC2_PUBLIC_IP>:3000`

---