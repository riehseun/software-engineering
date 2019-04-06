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
kubectl apply -f deployment.yaml

kubectl create -f service.yaml

kubectl get service # Get the port of Jenkins master

kubectl cluster-info | grep master

kubectl get pods | grep jenkins

kubectl describe pod <jenkins-pod>

kubectl get all
kubectl delete

kubectl exec -it <jenkins-pod> -- /bin/bash