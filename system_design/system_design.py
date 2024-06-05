from diagrams.aws.compute import EKS
from diagrams import Diagram, Cluster, Edge
from diagrams.k8s.compute import Pod
from diagrams.k8s.compute import Deploy as Deployment
from diagrams.k8s.compute import DS as Node
from diagrams.k8s.network import Service, Ingress
from diagrams.onprem.client import User
from diagrams.onprem.database import  Mongodb as Dynamodb
from diagrams.onprem.container import Docker
from diagrams.aws.compute import EC2
from diagrams.onprem.network import Nginx
from diagrams.saas.cdn import Cloudflare

with Diagram("Frontend and Backend Applications", show=False, outformat=["svg"], graph_attr={"bgcolor": "white"}) as diag:
    diag.dot.renderer = "cairo"
    user = User("User")

    with Cluster("Kubernetes Cluster"):
        with Cluster("Node 1"):
            ingress = Ingress("Ingress Controller")

            with Cluster("Backend Services"):
                backend_deployment = Deployment("Flask Deployment")
                flask_pods = [Pod("Flask API Pod 1"),
                              Pod("Flask API Pod 2"),
                              Pod("Flask API Pod 3")]
                backend_service = Service("Flask Service")
                dynamo_db = Dynamodb("DynamoDB")

            backend_deployment >> flask_pods
            backend_service >> backend_deployment
            flask_pods >> dynamo_db

        with Cluster("Node 2"):
            with Cluster("Frontend Services"):
                frontend_deployment = Deployment("Next.js Deployment")
                frontend_pods = [Pod("Next.js Pod 1"),
                                 Pod("Next.js Pod 2"),
                                 Pod("Next.js Pod 3")]
                frontend_service = Service("Next.js Service")

            frontend_deployment >> frontend_pods
            frontend_service >> frontend_deployment

    # Define interactions
    user >> Edge(label="requests") >> ingress
    ingress >> Edge(label="routes") >> frontend_service
    ingress >> Edge(label="API calls") >> backend_service

    frontend_service >> Edge(label="Generate") >> backend_service
    frontend_service >> Edge(label="Clear/Cancel") >> backend_service
    frontend_service >> Edge(label="Flask API Data") >> backend_service
    frontend_service >> Edge(label="DynamoDB Data") >> backend_service

    # Monitoring
    with Cluster("Monitoring"):
        prometheus = Docker("Prometheus")
        prometheus >> flask_pods
        prometheus >> frontend_pods

    # Other interactions
    user >> Edge(label="View Flask API Data") >> backend_service
    user >> Edge(label="View DynamoDB Data") >> backend_service
