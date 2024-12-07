from kubernetes import client, config

class KubernetesNamespacePods:
    def __init__(self, namespace):
        """
        Initialize with the specified namespace and load Kubernetes configuration.
        
        :param namespace: The namespace to query.
        """
        self.namespace = namespace
        # Load Kubernetes configuration
        config.load_kube_config()
        # Initialize CoreV1Api client
        self.v1_client = client.CoreV1Api()

    def list_pods(self):
        """
        List all pods in the initialized namespace.
        """
        try:
            pods = self.v1_client.list_namespaced_pod(self.namespace)
            print(f"Pods in namespace '{self.namespace}':")
            for pod in pods.items:
                print(f"- {pod.metadata.name}")
        except client.exceptions.ApiException as e:
            print(f"Exception when listing pods: {e}")

    def list_namespace(self):
        """
        List all namespaces.
        """
        try:
            namespaces = self.v1_client.list_namespace()
            print(f"Namespaces:")
            for namespace in namespaces.items:
                print(f"- {namespace.metadata.name}")
        except client.exceptions.ApiException as e:
            print(f"Exception when listing namespaces: {e}")

    def list_configmap(self):
        """
        List all configmaps in the initialized namespace.
        """
        try:
            configmaps = self.v1_client.list_namespaced_config_map(self.namespace)
            print(f"Configmaps in namespace '{self.namespace}':")
            for configmap in configmaps.items:
                print(f"- {configmap.metadata.name}")
        except client.exceptions.ApiException as e:
            print(f"Exception when listing configmaps: {e}")

    def list_secret(self):
        """
        List all secrets in the initialized namespace.
        """
        try:
            secrets = self.v1_client.list_namespaced_secret(self.namespace)
            print(f"Secrets in namespace '{self.namespace}':")
            for secret in secrets.items:
                print(f"- {secret.metadata.name}")
        except client.exceptions.ApiException as e:
            print(f"Exception when listing secrets: {e}")

if __name__ == "__main__":
    # Prompt user for namespace
    namespace = input("Enter the namespace: ").strip()
    # Create an instance of KubernetesNamespacePods
    kubernetes_namespace = KubernetesNamespacePods(namespace)
    # Call the method to list pods
    kubernetes_namespace.list_pods()
