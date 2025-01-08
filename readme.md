# Wikimedia Kafka to Elasticsearch Pipeline

## Project was conducted as part of a school project for "Advanced Big Data"

## Group : Anas Taqi & Ayoub Sarab

## Overview
This project implements a **real-time data pipeline** that streams recent changes from Wikimedia projects, processes the data, and indexes it into **Elasticsearch** for analysis. The pipeline uses **Kafka** for message streaming and is containerized using **Docker Compose**.

---

## Objectives
- **Stream Wikimedia Recent Changes** using **Server-Sent Events (SSE)**.
- Produce these events to **Apache Kafka**.
- Consume the events from Kafka and index them into **Elasticsearch**.
- Data visualization via **Kibana**.

---

## Technologies Used

| Technology       | Purpose                                           |
|-------------------|---------------------------------------------------|
| ![Kafka](https://upload.wikimedia.org/wikipedia/commons/6/64/Apache-kafka.svg) | Message streaming platform |
| ![Elasticsearch](https://upload.wikimedia.org/wikipedia/commons/f/f4/Elasticsearch_logo.svg) | Data indexing and search engine |
| ![Kibana](https://upload.wikimedia.org/wikipedia/commons/d/d0/Kibana_logo.svg) | Data visualization and analytics |
| ![Python](https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg) | Core implementation of producers and consumers |
| ![Docker](https://upload.wikimedia.org/wikipedia/commons/4/4e/Docker_%28container_engine%29_logo.svg) | Containerization and orchestration |

---

## Pipeline Workflow

1. **Wikimedia SSE to Kafka Producer**:
   - Connects to Wikimedia SSE stream.
   - Produces real-time events to a Kafka topic (`wikimedia-recentchange`).

2. **Kafka to Elasticsearch Consumer**:
   - Consumes events from Kafka.
   - Indexes the data into Elasticsearch for efficient search and analytics.

3. **Visualization**:
   - Use Kibana to explore and visualize indexed data.

---