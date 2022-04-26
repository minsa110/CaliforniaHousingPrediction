<!-- [![Open in Visual Studio Code](https://open.vscode.dev/badges/open-in-vscode.svg)](vscode://vscode.git/clone?url=https://github.com/minsa110/CaliforniaHousingPrediction.git)

_(^currently only works from cloned repo...)_ -->

# California housing prediction
### Goal of Analysis: Use ML algorithms to get best accuracy of predictions for California housing prices given the attributes in the dataset.

(Link to the [dataset](https://www.kaggle.com/camnugent/california-housing-prices) for California housing pricesc in 1990)

## Deploy the dockerized app to Azure (using Azure CLI)
1. Log in to Azure:
    ```
        az login
    ```
2. Create a new Azure Container Registry:
    ```
        az acr create --resource-group <somin-rg> --name <calidemo> --sku Basic
    ```
3. Log in to the created registry:
    ```
        az acr login -n <calidemo>
    ```
4. Create `deployment.yml` using [YAML reference for ACI](https://docs.microsoft.com/en-us/azure/container-instances/container-instances-reference-yaml), and get the password for the container registry using:
    ```
        az acr update -n <calidemo> --admin-enabled true
        az acr credential show --name <calidemo>
    ```
5. Create `nginx.conf` to reroute the web traffic to Streamlit's port 8501
6. Create a `Dockerfile` to install and setup all the resources needed to run the Streamlit app, including nginx
7. Build and push the image to the registry:
    ```
        docker build -t <azure_demo:v1> .
        docker tag azure_demo:v1 <calidemo>.azurecr.io/<azure_demo:v1>
        docker push <calidemo>.azurecr.io/<azure_demo:v1>
    ```
8. Deploy the app as an ACI:
    ```
        az container create --resource-group <somin-rg> --name <calidemo> -f deployment.yml
    ```
9. Confirm that your instance has been deployed using the Azure portal (navigate to [Container Instances](https://ms.portal.azure.com/#blade/HubsExtension/BrowseResource/resourceType/Microsoft.ContainerInstance%2FcontainerGroups)) and/or access the live ML app 🥳:
    ```
        <calihouseprice90>.westus2.azurecontainer.io
    ```
