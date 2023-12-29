from kubernetes import client, config

def update_deployment_strategy(deployment_name, namespace, max_unavailable):
    config.load_kube_config()
    apps_v1 = client.AppsV1Api()

    deployment = apps_v1.read_namespaced_deployment(deployment_name, namespace)
    deployment.spec.strategy.rolling_update.max_unavailable = max_unavailable
    apps_v1.patch_namespaced_deployment(deployment_name, namespace, deployment)

if __name__ == "__main__":
    update_deployment_strategy('my-deployment', 'my-namespace', '25%')

"""Los archivos YAML son la columna vertebral para definir y administrar recursos. Sin embargo, los archivos YAML estáticos
pueden ser limitantes, especialmente cuando necesita administrar diferentes configuraciones para diferentes entornos o
escenarios de implementación. Aquí es donde entra Python, que ofrece un enfoque dinámico y flexible para parametrizar sus archivos YAML.

Por ejemplo, puede personalizar su estrategia de actualización continua utilizando Python con el siguiente código de ejemplo."""
