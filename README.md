# **OmniMed**

<p align="center">
  <img src="./assets/logo.png" alt="Logo" width="400">
</p>

Une plateforme dédiée aux analyses bioinformatiques et médicales, intégrant des pipelines d'analyse de séquences génomiques, la modélisation de protéines et l'identification d'épitopes immunogènes, le tout orchestré avec Python, React, GraphQL, PostgreSQL sous Docker, Kubernetes pour la scalabilité, et un pipeline CI/CD optimisé pour la recherche biomédicale avancée.

---

## **Arborescence du projet**

Voici l’organisation du projet :

```
project-root/
│
├── frontend/          # Code source de l'application React (interface utilisateur)
├── backend/           # API en Python pour les analyses médicales et bioinformatiques
├── db/                # Configuration de la base de données PostgreSQL
├── k8s/               # Manifests Kubernetes pour le déploiement
├── scripts/           # Scripts utilitaires (ex. : migration, initialisation)
├── docker-compose.yml # Configuration Docker pour le développement local
└── README.md          # Documentation du projet
```

---

## **Descriptions des dossiers**

### **`frontend/`**
- Contient le code source de l'application React.
- Connecté à l'API GraphQL pour afficher les résultats d'analyses en temps réel.
- Configuration d'Apollo Client pour les requêtes GraphQL.

### **`backend/`**
- Code Python utilisant Flask ou FastAPI pour gérer :
  - Analyse de séquences génomiques.
  - Modélisation de protéines.
  - Identification d'épitopes immunogènes.
- Intègre des bibliothèques comme `Biopython` pour les calculs bioinformatiques.

### **`db/`**
- Configuration de la base de données PostgreSQL.
- Stocke les séquences génomiques, les résultats d'analyses et les logs.

### **`k8s/`**
- Manifests Kubernetes pour le déploiement (Deployments, Services, Ingress).
- Gère la scalabilité et la résilience du système.

### **`scripts/`**
- Scripts d’automatisation :
  - Initialisation des données.
  - Maintenance ou migrations de base de données.

---

## **Installation et démarrage**

### **Prérequis**
1. [Docker](https://www.docker.com/) et [Docker Compose](https://docs.docker.com/compose/) installés.
2. [Python 3.10+](https://www.python.org/) installé localement (pour le développement backend).
3. [Node.js 18+](https://nodejs.org/) pour le développement frontend.
4. [kubectl](https://kubernetes.io/docs/tasks/tools/) et un cluster Kubernetes (optionnel pour déploiement).

### **Démarrer le projet (localement avec Docker Compose)**
1. Clonez ce repository :
   ```bash
   git clone https://github.com/votre-username/nom-du-repository.git
   cd nom-du-repository
   ```
2. Démarrez les services avec Docker Compose :
   ```bash
   docker-compose up --build
   ```
3. Accédez aux services :
   - **Frontend** : [http://localhost:3000](http://localhost:3000)
   - **Backend** : [http://localhost:4000](http://localhost:4000)