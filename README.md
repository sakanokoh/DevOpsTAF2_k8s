# Gestion des Étudiants avec FastAPI et MySQL
Bienvenue dans le dépôt **DevOpsTAF2_K8s** ! Ce projet contient une application backend construite avec FastAPI, une base de données MySQL, et est déployé sur Kubernetes.

## Description

Ce projet propose une API REST développée avec FastAPI et MySQL, permettant de réaliser des opérations CRUD (Create, Read, Update, Delete) sur des étudiants. L'API expose des endpoints pour ajouter, consulter, mettre à jour et supprimer des étudiants dans une base de données MySQL.

## Fonctionnalités

- **Création d'un étudiant** : Ajouter un nouvel étudiant dans la base de données.
- **Consultation des étudiants** : Récupérer la liste complète des étudiants ou un étudiant spécifique par son ID.
- **Suppression d'un étudiant** : Supprimer un étudiant en fonction de son ID.

## Prérequis

Avant de commencer, assurez-vous d'avoir installé les éléments suivants :

- [Docker](https://www.docker.com/get-started)
- [kubectl](https://kubernetes.io/docs/tasks/tools/)
- [Minikube](https://minikube.sigs.k8s.io/docs/start/) (ou un autre orchestrateur Kubernetes)

## URL du dépôt

Vous pouvez accéder au dépôt GitHub à l'adresse suivante : [https://github.com/sakanokoh/DevOpsTAF2_k8s.git](https://github.com/sakanokoh/DevOpsTAF2_k8s.git)

## Image Docker

L'image Docker pour le backend est disponible sous le nom : 
```
hamsak/backendtaf2:v2.0.0
```

## Déploiement de l'application

### Étape 1 : Cloner le dépôt

Clonez ce dépôt sur votre machine locale :

```bash
git clone https://github.com/sakanokoh/DevOpsTAF2_k8s.git
cd DevOpsTAF2_k8s
```

### Étape 2 : Construire et exécuter l'image Docker (facultatif)

Si vous souhaitez exécuter l'image Docker localement pour le développement ou les tests, utilisez les commandes suivantes :

```bash
docker build -t hamsak/backendtaf2:v2.0.0 .
```

### Étape 3 : Déployer sur Kubernetes

Assurez-vous que votre cluster Kubernetes est en cours d'exécution (par exemple, avec Minikube).
Si non exécuter cette commande suivante pour créer un cluster avec 3 noeuds en utilisant `Docker` comme driver

```bash
minikube start --nodes 3 --driver=docker
```

Ensuite, appliquez les manifestes Kubernetes :

```bash
kubectl apply -f k8s/
```

### Étape 4 : Vérifier les déploiements

Vérifiez que les déploiements sont en cours d'exécution :

```bash
kubectl get deployments
kubectl get services
```

### Étape 5 : Accéder à l'application

Pour accéder à l'application FastAPI, utilisez l'adresse suivante dans votre navigateur :

```
http://<adresse_ip>:8000
```

Remplacez `<adresse_ip>` par l'adresse IP de votre service Kubernetes ou l'adresse de votre Minikube.

## Configuration

### Variables d'environnement

Les configurations pour l'application et la base de données sont gérées par des ConfigMaps et Secrets Kubernetes. Voici les fichiers concernés :

- **backend-secret.yaml** : Contient les secrets liés à l'application backend, comme l'utilisateur et le mot de passe de la base de données.
  
- **backend-configmap.yaml** : Contient les configurations pour l'application backend, comme l'hôte et le nom de la base de données.

- **database-secret.yaml** : Contient les secrets liés à la base de données MySQL, comme le mot de passe root et les informations d'identification de l'utilisateur.

- **database-configmap.yaml** : Contient les configurations pour la base de données, comme le nom de la base de données et l'hôte.

Assurez-vous que ces fichiers sont correctement configurés avant de déployer l'application. Les secrets doivent être encodés en base64.

## Notes supplémentaires

- Si vous utilisez Minikube, vous pouvez obtenir l'adresse IP de votre cluster avec la commande :

  ```bash
  minikube ip
  ```

- Pour vérifier les logs de vos déploiements, utilisez la commande :

  ```bash
  kubectl logs <nom_du_pod>
  ```
