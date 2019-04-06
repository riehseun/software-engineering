# https://rancher.com/blog/2018/2018-11-27-scaling-jenkins/

########## ---------- From Docker Enabled local Unix machine ---------- ##########

vi Dockerfile-jenkins-master

# FROM jenkins/jenkins:lts

# # Plugins for better UX (not mandatory)
# RUN /usr/local/bin/install-plugins.sh ansicolor
# RUN /usr/local/bin/install-plugins.sh greenballs

# # Plugin for scaling Jenkins agents
# RUN /usr/local/bin/install-plugins.sh kubernetes

# USER jenkins

touch empty-test-file
vi Dockerfile-jenkins-slave-jnlp1

# FROM jenkins/jnlp-slave

# # For testing purpose only
# COPY empty-test-file /jenkins-slave1

# ENTRYPOINT ["jenkins-slave"]

vi Dockerfile-jenkins-slave-jnlp2

# FROM jenkins/jnlp-slave

# # For testing purpose only
# COPY empty-test-file /jenkins-slave2

# ENTRYPOINT ["jenkins-slave"]

docker build -f Dockerfile-jenkins-master -t riehseun/jenkins-master .

docker images

docker login

docker push riehseun/jenkins-master

docker build -f Dockerfile-jenkins-slave-jnlp1 -t riehseun/jenkins-slave-jnlp1 .
docker push riehseun/jenkins-slave-jnlp1

docker build -f Dockerfile-jenkins-slave-jnlp2 -t riehseun/jenkins-slave-jnlp2 .
docker push riehseun/jenkins-slave-jnlp2

vi deployment.yaml

# apiVersion: extensions/v1beta1
# kind: Deployment
# metadata:
#   name: jenkins
# spec:
#   replicas: 1
#   template:
#     metadata:
#       labels:
#         app: jenkins
#     spec:
#       containers:
#         - name: jenkins
#           image: riehseun/jenkins-master
#           env:
#             - name: JAVA_OPTS
#               value: -Djenkins.install.runSetupWizard=false
#           ports:
#             - name: http-port
#               containerPort: 8080
#             - name: jnlp-port
#               containerPort: 50000
#           volumeMounts:
#             - name: jenkins-home
#               mountPath: /var/jenkins_home
#       volumes:
#         - name: jenkins-home
#           emptyDir: {}

vi service.yaml

# apiVersion: v1
# kind: Service
# metadata:
#   name: jenkins
# spec:
#   type: LoadBalancer
#   ports:
#     - port: 80
#       targetPort: 8080
#   selector:
#     app: jenkins

# ---

# apiVersion: v1
# kind: Service
# metadata:
#   name: jenkins-jnlp
# spec:
#   type: ClusterIP
#   ports:
#     - port: 50000
#       targetPort: 50000
#   selector:
#     app: jenkins



# https://www.blazemeter.com/blog/how-to-setup-scalable-jenkins-on-top-of-a-kubernetes-cluster

# FROM k8s master
kubectl apply -f deployment.yaml

kubectl create -f service.yaml

kubectl get service # Get the port of Jenkins master

kubectl cluster-info | grep master

kubectl get pods | grep jenkins

kubectl describe pod <jenkins-pod>

kubectl delete