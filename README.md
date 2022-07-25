# California housing prediction
Goal of Analysis: Use ML algorithms to get best accuracy of predictions for California housing prices (in 1990) given the attributes in the dataset. (Link to the [dataset](https://www.kaggle.com/camnugent/california-housing-prices))

**Live site: http://calihouseprice90.westus2.azurecontainer.io/**<br>
(Note: different URL from the one shared during talk since that resource has now been deleted)

Sign up today for your free Azure account and receive 12 months of free popular services, $200 free credit and 25+ always free services 👉 [Start Free](https://azure.microsoft.com/free/open-source).

## Cool/useful VS Code extensions mentioned
Developed by the VS Code team:
- [Jupyter](https://marketplace.visualstudio.com/itemdetails?itemName=ms-toolsai.jupyter) - turn any Python env into a Jupyter kernel + cool features mentioned during the talk
- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) - first-class Python experience support

Developed by the community:
- [Python Environment Manager](https://marketplace.visualstudio.com/items?itemName=donjayamanne.python-environment-manager) - manage Python environments and packages
- [Marp for VS Code](https://marketplace.visualstudio.com/items?itemName=marp-team.marp-vscode) - create a deck using markdown (used for the talk)
- [vscode-reveal](https://marketplace.visualstudio.com/items?itemName=evilz.vscode-reveal) - create a deck using markdown (NOT used for talk, but worth mentioning)
- Data viewing tools
   - [Excel Viewer](https://marketplace.visualstudio.com/items?itemName=GrapeCity.gc-excelviewer) - custom editor / previews for CSV files and Excel spreadsheets
   - [Excel to Markdown table](https://marketplace.visualstudio.com/items?itemName=csholmq.excel-to-markdown-table) - paste a table from CSV / Excel files directly to a markdown file via Shift + Alt + V

Work with Azure:
- [Azure Account](https://marketplace.visualstudio.com/items?itemName=ms-vscode.azure-account) - SSO / account management
- [Azure Resources](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azureresourcegroups) - subscription / resource management
- [Docker](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker) - work with Docker

My favorite VS Code themes for notebooks:
- Dark: [One Monokai Theme](https://marketplace.visualstudio.com/items?itemName=azemoh.one-monokai)
- Light: [Snazzy Light](https://marketplace.visualstudio.com/items?itemName=loilo.snazzy-light)

Other helpful links:
- [Choose an Azure compute service](https://docs.microsoft.com/en-us/azure/architecture/guide/technology-choices/compute-decision-tree) for your needs
- Create an Azure Container Instances deployment definition file using the [ACI schema](https://docs.microsoft.com/en-us/azure/container-instances/container-instances-reference-yaml)<br>To get your ACR's username and password for the yaml file:
   ```python
   az acr update -n wwc2207 --admin-enabled true
   az acr credential show --name wwc2207 --resource-group wwc2207
   ```
- [Enable HTTPS](https://docs.microsoft.com/en-us/azure/container-instances/container-instances-container-group-ssl) with nginx and self-signed certificate

## Deploy the dockerized app to Azure
An alternative way of deploying to ACI on VS Code without the extension (using Azure CLI instead)

1. Log in to Azure:
    ```
        az login
    ```
2. Create a new Azure Container Registry:
    ```
        az acr create --resource-group <resource group name> --name <container registry name> --sku Basic
    ```
3. Log in to the created registry:
    ```
        az acr login -n <container registry name>
    ```
4. Create `deployment.yml` using [YAML reference for ACI](https://docs.microsoft.com/en-us/azure/container-instances/container-instances-reference-yaml), and get the password for the container registry using:
    ```
        az acr update -n <container registry name> --admin-enabled true
        az acr credential show --name <container registry name>
    ```
5. Create `nginx.conf` to reroute the web traffic to Streamlit's port 8501
6. Create a `Dockerfile` to install and setup all the resources needed to run the Streamlit app, including nginx
7. Build and push the image to the registry:
    ```
        docker build -t <image name> .
        docker tag image name <container registry name>.azurecr.io/<image name>
        docker push <container registry name>.azurecr.io/<image name>
    ```
8. Deploy the app as an ACI:
    ```
        az container create --resource-group <resource group name> --name <container registry name> -f deployment.yml
    ```
9. Confirm that your instance has been deployed using the Azure portal (navigate to [Container Instances](https://ms.portal.azure.com/#blade/HubsExtension/BrowseResource/resourceType/Microsoft.ContainerInstance%2FcontainerGroups)) and/or access the live ML app 🥳:
    ```
        <DNS name>.westus2.azurecontainer.io
    ```

## The “dot” (github.dev) and Pyodide
Press '.' on your keyboard to try it out!
- [vscode-pyodide - Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=joyceerhl.vscode-pyodide) (Pyolite kernel)
- Install packages from PyPI with micropip
- Load publicly available csv / json file
- Spin up [Codespaces](https://github.com/features/codespaces) for full VS Code features with GitHub compute backing it

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
