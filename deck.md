---
marp: true
style: |
    img[alt~="center"] {
      display: block;
      margin: 0 auto;
    },
    section{
      justify-content: flex-start;
    },
    section.lead h2 {
      text-align: center;
    },
    section.center {
      text-align: center;
    }

---
![bg](deck-content/Intro.png)

---
# Quick overview
1. Why would I use notebooks in VS Code?
2. How do I create my ML app?
3. How do I containerize by ML app?
4. How do I deploy my ML app?
<br><br>
Cover all without leaving VS Code 😉

![bg right:34%](deck-content/webapp.png)

---
<!-- _class: lead -->
# Why use notebooks in VS Code?
- Extension marketplace
- Debugging (extends to nb experiences)
- Embedded git control
- IntelliSense
- Integrated terminal
- First-class Python support
- Code refactoring
- Highly customizable (themes, keyboard shortcuts)

## Code editor + [Jupyter Notebooks](https://marketplace.visualstudio.com/itemdetails?itemName=ms-toolsai.jupyter) = ❤️

---
## Starting a notebook in VS Code is a _little_ different

| Classic Jupyter Notebooks | Notebooks in VS Code |
|:-------------------------:|:--------------------:|
| Create a Python environment<br>`conda create -n myenv`</br></br> | Create a Python environment<br>`conda create -n myenv`</br></br>|
| Activate the Python environment<br>`conda activate myenv`</br></br> | Open VS Code<br>`code .`</br></br> |
| Launch Jupyter Notebooks<br>`jupyter notebook`</br></br> | Select a Python environment</br></br>|

---
<br><br><br><br>

# California housing prediction

### Goal of Analysis: Use ML algorithms to get best accuracy of predictions for California housing prices (in 1990) given the attributes in the dataset.

(Link to the [dataset](https://www.kaggle.com/camnugent/california-housing-prices))

---
# Notebook contents
- Quick look at the data
- Data visualization
- Data cleaning
- ML training and evaluating
- ML model export

###### _Attribute the content of this notebook to [Hands-on Machine Learning with Scikit-Learn, Keras & Tensorflow](https://github.com/ageron/handson-ml2) by Aurelien Geron_

![bg w:550 right:45%](images/cali-heatmap.png)

---
```python
    # visualize data based on geographical info
    import matplotlib.image as mpimg
    import matplotlib.pyplot as mppyplot

    california_img=mpimg.imread('./images/california.png')
    ax = housing.plot(kind="scatter", x="longitude", y="latitude", figsize=(10,7),
                    s=housing['population']/100, label="Population",
                    c="median_house_value", cmap=plt.get_cmap("jet"),
                    colorbar=False, alpha=0.4)
    plt.imshow(california_img, extent=[-124.55, -113.80, 32.45, 42.05], alpha=0.5,
            cmap=plt.get_cmap("jet"))
    plt.ylabel("Latitude", fontsize=14)
    plt.xlabel("Longitude", fontsize=14)

    prices = housing["median_house_value"]
    tick_values = np.linspace(prices.min(), prices.max(), 11)
    cbar = plt.colorbar(ticks=tick_values/prices.max())
    cbar.ax.set_yticklabels(["$%dk"%(round(v/1000)) for v in tick_values], fontsize=14)
    cbar.set_label('Median House Value', fontsize=16)

    plt.legend(fontsize=16)
    plt.show()
```
---
![w:500 center](images/california.png)