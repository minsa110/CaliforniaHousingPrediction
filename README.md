<!-- [![Open in Visual Studio Code](https://open.vscode.dev/badges/open-in-vscode.svg)](vscode://vscode.git/clone?url=https://github.com/minsa110/CaliforniaHousingPrediction.git)

_(^currently only works from cloned repo...)_ -->

# California housing prediction
Goal of Analysis: Use ML algorithms to get best accuracy of predictions for California housing prices given the attributes in the dataset. (Link to the [dataset](https://www.kaggle.com/camnugent/california-housing-prices) for California housing prices in 1990)

Live site: http://calihouseprice90.westus2.azurecontainer.io/

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

## Create and attach to an AML compute (from VS Code)
1. Create a compute instance through the [AML extension](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.vscode-ai) using the [AML YAML configuration spec](https://docs.microsoft.com/en-us/azure/machine-learning/reference-yaml-core-syntax) (can also be done through the Azure portal), for example:
    ```yaml
        $schema: https://azuremlschemas.azureedge.net/latest/computeInstance.schema.json
        name: california-housing
        type: computeinstance
        size: Standard_DS3_v2
    ```
2. Connect to that compute instance from VS Code (right click on compute instance and click "Connect")
3. Trust folder authors and... you're connected! 🙌🏻
4. (Optional) Verify connection via remote window indicator (bottom left), and/or type `pwd` in the terminal
5. (Optional) Debug within the AML compute, directly from VSC
6. (Optional) Load a local directory and execute a file against a specified compute target through a [`command job`](https://docs.microsoft.com/en-us/cli/azure/ml/job?view=azure-cli-latest) using the [AML YAML configuration spec](https://docs.microsoft.com/en-us/azure/machine-learning/reference-yaml-job-command), for example:
    ```yaml
        $schema: https://azuremlschemas.azureedge.net/latest/commandJob.schema.json
        code: ./
        command: python test.py
        environment: azureml:AzureML-PyTorch-1.3-CPU:40
        compute: azureml: somin-aml-compute
    ```
