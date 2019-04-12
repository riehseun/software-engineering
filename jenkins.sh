# https://rancher.com/blog/2018/2018-11-27-scaling-jenkins/

########## ---------- From Docker Enabled local Unix machine ---------- ##########

vi Dockerfile-jenkins-master

touch empty-test-file
vi Dockerfile-jenkins-slave-jnlp1

vi Dockerfile-jenkins-slave-jnlp2

docker build -f Dockerfile-jenkins-master -t riehseun/jenkins-master .

docker images

docker login

docker push riehseun/jenkins-master

docker build -f Dockerfile-jenkins-slave-jnlp1 -t riehseun/jenkins-slave-jnlp1 .
docker push riehseun/jenkins-slave-jnlp1

docker build -f Dockerfile-jenkins-slave-jnlp2 -t riehseun/jenkins-slave-jnlp2 .
docker push riehseun/jenkins-slave-jnlp2

vi deployment.yaml

vi service.yaml

# https://www.blazemeter.com/blog/how-to-setup-scalable-jenkins-on-top-of-a-kubernetes-cluster

# FROM k8s master
kubectl create -f jenkins-namespace.yaml (use "apply" for update)
kubectl create -f jenkins-deployment.yaml
kubectl create -f jenkins-service.yaml
kubectl get pods --namespace jenkins
kubectl get all -n jenkins


kubectl get service # Get the port of Jenkins master

kubectl cluster-info | grep master

kubectl get pods | grep jenkins

kubectl describe pod <jenkins-pod>

kubectl get all
kubectl delete

kubectl exec -it <jenkins-pod> -- /bin/bash

kubectl get pods/<podname> -o yaml
kubectl get services/<servicename> -o yaml



kubectl -n kube-system logs <jenkins-pod>

kubectl logs <jenkins-pod> -c jnlp


# Givng "default" service account access to connect to k8s master
kubectl create clusterrolebinding permissive-binding --clusterrole=cluster-admin --user=admin --user=kubelet --group=system:serviceaccounts:default
Kubernetes URL : https://10.26.2.2:6443 (kubectl cluster-info)
Jenkins tunnel : 104.196.0.154:50000 (kubectl get svc)














## SAMPLE JOB
def label = "worker-${UUID.randomUUID().toString()}"
podTemplate(label: label, containers: [
  containerTemplate(name: 'jenkins-slave', image: 'jenkinsci/jnlp-slave', command: 'cat', ttyEnabled: true),
],
volumes: [
  hostPathVolume(mountPath: '/var/run/docker.sock', hostPath: '/var/run/docker.sock')
]) {
  node(label) {
    stage('Test') {
      try {
        container('jenkins-slave') {
          sh """
            echo hi
            """
        }
      }
      catch (exc) {
        println "Failed to test - ${currentBuild.fullDisplayName}"
        throw(exc)
      }
    }
  }
}