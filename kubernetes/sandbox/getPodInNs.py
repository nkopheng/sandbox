from kubernetes import client, config
from rich.traceback import install
install(show_locals=True)

def list_pods_in_namespace(namespace):
    """
    List all pods in the specified Kubernetes namespace.

    :param namespace: The namespace to query.
    """
    # Load the Kubernetes configuration from the default kubeconfig file
    config.load_kube_config()

    # Initialize the CoreV1Api client
    v1 = client.CoreV1Api()

    try:
        # List pods in the specified namespace
        pods = v1.list_namespaced_pod(namespace)
        print(f"Pods in namespace '{namespace}':")
        for pod in pods.items:
            print(f"- {pod.metadata.name}")
    except client.exceptions.ApiException as e:
        print(f"Exception when listing pods: {e}")

if __name__ == "__main__":
    # Specify the namespace you want to query
    namespace = input("Enter the namespace: ").strip()
    list_pods_in_namespace(namespace)

