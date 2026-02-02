ARGUS 
Real-Time Fraud Detection MLOps System


Overview:
ARGUS is an end-to-end real-time fraud detection MLOps system designed to simulate how fraud detection models operate in production fintech environments.
Unlike traditional machine learning projects that focus primarily on model accuracy, ARGUS emphasizes production-grade MLOps practices such as real-time feature serving, safe model deployment, continuous monitoring, concept drift detection, and automated retraining.
Fraud patterns evolve rapidly, causing static models to degrade over time. ARGUS addresses this challenge by enabling continuous learning and safe model promotion using streaming data and monitoring pipelines.

Problem Statement:

Fraud detection systems in fintech environments face several challenges:

>Rapidly changing fraud patterns (concept drift)
>High-throughput and low-latency inference requirements
>Risky deployments where incorrect models can lead to financial loss
>The need for continuous monitoring and automated retraining
ARGUS demonstrates how these challenges are addressed using modern MLOps architecture.

System Architecture:
ARGUS is built around two interconnected pipelines.

Real-Time Inference Pipeline

   >Exposes a FastAPI service for fraud predictions

   >Retrieves real-time features from a Feast feature store backed by Redis

   >Executes two models in parallel:

        >Champion model for live decision-making

        >Shadow model for silent performance evaluation

   >Streams prediction events to Kafka for monitoring and analysis

Continuous Learning Pipeline

 >Consumes live transaction streams from Kafka

 >Monitors feature and prediction distributions

 >Detects data and concept drift

 >Triggers retraining workflows using Apache Airflow

 >Deploys newly trained models in shadow mode prior to promotion

Architecture Flow:

Transaction Request
- FastAPI Inference Service
- Feast Feature Store (Redis)
- Champion Model (Fraud Decision)
- Shadow Model (Silent Evaluation)
- Kafka Event Stream
- Monitoring and Drift Detection
- Airflow Retraining Pipeline
- Shadow Deployment and Champion Promotion


Technology Stack:
>Python 3.11
>FastAPI with Swagger UI
>XGBoost
>Feast Feature Store
>Redis
>Apache Kafka
>Docker 
>Apache Airflow

MLOps Concepts Demonstrated:
>Feature store integration
>Online and offline feature consistency
>Real-time inference serving
>Shadow deployment and model comparison
>Concept drift detection
>Streaming-based monitoring
>Automated retraining workflows
>Production-oriented project structure

API Usage:
Start the inference service
uvicorn app:app --reload

Swagger UI
http://127.0.0.1:8000/docs

Example Prediction Request
POST /predict?user_id=user_1&amount=90000

Project Structure
ARGUS/
- app.py
- train_model.py
- train_model_v2.py
- drift_detector.py
- auto_retrain.py
- kafka_producer.py
- kafka_consumer.py
- shadow_logger.py
- airflow/
- argus_feature_store/
- README.md


Evaluation Focus:
ARGUS prioritizes system reliability, deployment safety, and continuous learning over isolated accuracy metrics.
The project reflects how real-world fintech fraud detection systems are designed, deployed, monitored, and maintained in production environments.

Future Improvements:
>Canary deployments for gradual model rollout
>Advanced drift detection techniques
>Model performance dashboards
>Feature freshness monitoring
>Integration with real-world payment datasets

Author
Anjali