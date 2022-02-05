# %% [markdown]
# # California housing prediction
# ### Goal of Analysis: Use machine learning algorithms to get best accuracy of predictions for California housing prices given the attributes in the dataset.
# 
# (Note: link to the [dataset](https://www.kaggle.com/camnugent/california-housing-prices))

# %% [markdown]
# ## Loading data

# %%
import pandas as pd

housing = pd.read_csv('./data/housing.csv')

# %% [markdown]
# ## Quick look at the data

# %%
housing.head()

# %%
housing.info()

# %% [markdown]

# Look at data frame

# %%
# get summary of numerical attributes
housing.describe()

# %%
# histogram for each numerical attribute
import matplotlib.pyplot as plt
housing.hist(bins=50, figsize=(20,15))
plt.show()

# %% [markdown]
# ## Creating a test set using stratified sampling

# %%
# create an income category attribute with 5 categories (labeled from 1 to 5)
# FYI about the data 1.5 = $15,000
import numpy as np

housing["income_cat"] = pd.cut(housing["median_income"],
                               bins=[0., 1.5, 3.0, 4.5, 6., np.inf],
                               labels=[1, 2, 3, 4, 5])
housing["income_cat"].value_counts()

# %%
housing["income_cat"].hist()

# %%
# stratified sampling based on income category
from sklearn.model_selection import StratifiedShuffleSplit

split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
for train_index, test_index in split.split(housing, housing["income_cat"]):
    strat_train_set = housing.loc[train_index]
    strat_test_set = housing.loc[test_index]

strat_test_set["income_cat"].value_counts() / len(strat_test_set)

# %%
# remove the income_cat attribute so the data is back to its original state

for set_ in (strat_train_set, strat_test_set):
    set_.drop("income_cat", axis=1, inplace=True)

# %% [markdown]
# ## Visualizing data for insights

# %%
# create a copy of the test set to only explore the training set
housing = strat_train_set.copy()

# %%
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

# %% [markdown]
# ## Looking for correlations

# %%
corr_matrix = housing.corr() # std correlation coefficient
corr_matrix["median_house_value"].sort_values(ascending=False)

# %%
import seaborn as sns

fig = plt.figure(figsize=(20, 5))

# (Corr= 0.135097) total_rooms vs. median_house_value
fig1 = fig.add_subplot(131)
sns.scatterplot(x = housing.total_rooms, y = housing.median_house_value, hue=housing.median_income, palette= 'Spectral')

# (Corr= 0.114110) housing_median_age vs. median_house_value
fig2 = fig.add_subplot(132)
sns.scatterplot(x = housing.housing_median_age, y = housing.median_house_value, hue=housing.median_income, palette= 'Spectral')

# (Corr= 0.064506) households vs. median_house_value
fig3 = fig.add_subplot(133)
sns.scatterplot(x = housing.households, y = housing.median_house_value, hue=housing.median_income, palette= 'Spectral')

# %%
housing["rooms_per_household"] = housing["total_rooms"]/housing["households"]
housing["bedrooms_per_room"] = housing["total_bedrooms"]/housing["total_rooms"]
housing["population_per_household"]=housing["population"]/housing["households"]

corr_matrix = housing.corr()
corr_matrix["median_house_value"].sort_values(ascending=False)

# %% [markdown]
# ## Data cleaning

# %%
# first revert to a clean training set
housing = strat_train_set.drop("median_house_value", axis=1) # drop labels for training set
housing_labels = strat_train_set["median_house_value"].copy()

# %%
# take care of missing values in the training set, saving the median value that's been computed
# using SimpleImputer from Scikit-Learn
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(strategy="median")

# %%
# Remove the text attribute because median can only be calculated on numerical attributes:
housing_num = housing.drop("ocean_proximity", axis=1)

# %%
# fit the imputer instance to the training data using the fit() method
imputer.fit(housing_num)

# %%
# to be safe, apply imputer to all numerical attributes
imputer.statistics_

# %%
housing_num.median().values

# %%
# use this "trained" imputer to transform the training set by
# replacing missing values with the learned medians
X = imputer.transform(housing_num)

# %%
# result ^ is a plain NumPy array containing the transformed features
# put it back into a pandas DataFrame doing this:
housing_tr = pd.DataFrame(X, columns=housing_num.columns, index=housing.index)

# %% [markdown]
# ## Handling text and categorical attributes

# %%
# convert categorical values (ocean proximity) into numbers

from sklearn.preprocessing import OrdinalEncoder

housing_cat = housing[["ocean_proximity"]]
ordinal_encoder = OrdinalEncoder()
housing_cat_encoded = ordinal_encoder.fit_transform(housing_cat)
housing_cat_encoded[:10]

# %%
# create one binary attribute per category since we don't want ML algorithms to assume that two nearby values are more similar than two distant values
from sklearn.preprocessing import OneHotEncoder

cat_encoder = OneHotEncoder()
housing_cat_1hot = cat_encoder.fit_transform(housing_cat)
housing_cat_1hot

# %%
# convert the SciPy sparse matrix from ^ to (dense) NumPy array
housing_cat_1hot.toarray()

# %% [markdown]
# ## Custom transformers

# %%
# custom transformer to add extra attributes
from sklearn.base import BaseEstimator, TransformerMixin

# column index
rooms_ix, bedrooms_ix, population_ix, households_ix = 3, 4, 5, 6

class CombinedAttributesAdder(BaseEstimator, TransformerMixin):
    def __init__(self, add_bedrooms_per_room=True): # no *args or **kargs
        self.add_bedrooms_per_room = add_bedrooms_per_room
    def fit(self, X, y=None):
        return self  # nothing else to do
    def transform(self, X):
        rooms_per_household = X[:, rooms_ix] / X[:, households_ix]
        population_per_household = X[:, population_ix] / X[:, households_ix]
        if self.add_bedrooms_per_room:
            bedrooms_per_room = X[:, bedrooms_ix] / X[:, rooms_ix]
            return np.c_[X, rooms_per_household, population_per_household,
                         bedrooms_per_room]
        else:
            return np.c_[X, rooms_per_household, population_per_household]

attr_adder = CombinedAttributesAdder(add_bedrooms_per_room=False)
housing_extra_attribs = attr_adder.transform(housing.values)

# %% [markdown]
# ## Feature scaling & transformation pipelines

# %%
# build pipeline for prepocessing numerical attributes
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

num_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy="median")),
        ('attribs_adder', CombinedAttributesAdder()),
        ('std_scaler', StandardScaler()),
    ])

housing_num_tr = num_pipeline.fit_transform(housing_num)

# %%
# use `ColumnTransformer` to conveniently have a single transformer handle all columns
from sklearn.compose import ColumnTransformer

num_attribs = list(housing_num)
cat_attribs = ["ocean_proximity"]

full_pipeline = ColumnTransformer([
        ("num", num_pipeline, num_attribs),
        ("cat", OneHotEncoder(), cat_attribs),
    ])

housing_prepared = full_pipeline.fit_transform(housing)

# %%
housing_prepared

# %%
housing_prepared.shape

# %% [markdown]
# ## Training and evaluating on the training set

# %%
# Linear Regression model
from sklearn.linear_model import LinearRegression

lin_reg = LinearRegression()
lin_reg.fit(housing_prepared, housing_labels)

# %%
# try the full preprocessing pipeline on a few training instances
some_data = housing.iloc[:5]
some_labels = housing_labels.iloc[:5]
some_data_prepared = full_pipeline.transform(some_data)

print("Predictions:", lin_reg.predict(some_data_prepared))

# %%
# compare against actual values
print("Labels:", list(some_labels))

# %%
# measure this regression model's RMSE
from sklearn.metrics import mean_squared_error

housing_predictions = lin_reg.predict(housing_prepared)
lin_mse = mean_squared_error(housing_labels, housing_predictions)
lin_rmse = np.sqrt(lin_mse)
lin_rmse

# %%
# train using `DecisionTreeRegressor` that is capable of finding complex nonlinear relationships in the data

from sklearn.tree import DecisionTreeRegressor

tree_reg = DecisionTreeRegressor(random_state=42)
tree_reg.fit(housing_prepared, housing_labels)

housing_predictions = tree_reg.predict(housing_prepared)
tree_mse = mean_squared_error(housing_labels, housing_predictions)
tree_rmse = np.sqrt(tree_mse)
tree_rmse

# %% [markdown]
# ^ No error at all? Probably badly overfits the data...

# %%
# better evaluate using cross-validation by splitting the training set into a smaller training set and a validation set
# can use `train_test_split()`, or alternatively Scikit-Learn's K-fold cross-validation feature
from sklearn.model_selection import cross_val_score

scores = cross_val_score(tree_reg, housing_prepared, housing_labels,
                         scoring="neg_mean_squared_error", cv=10)
tree_rmse_scores = np.sqrt(-scores)

# %%
# looking at the results...
def display_scores(scores):
    print("Scores:", scores)
    print("Mean:", scores.mean())
    print("Standard deviation:", scores.std())

display_scores(tree_rmse_scores)

# %%
# actually performs worse than the linear regression model
lin_scores = cross_val_score(lin_reg, housing_prepared, housing_labels,
                             scoring="neg_mean_squared_error", cv=10)
lin_rmse_scores = np.sqrt(-lin_scores)
display_scores(lin_rmse_scores)

# %%
# try a different model, `RandomForestRegressor`
from sklearn.ensemble import RandomForestRegressor

forest_reg = RandomForestRegressor(n_estimators=100, random_state=42)
forest_reg.fit(housing_prepared, housing_labels)

# %%
housing_predictions = forest_reg.predict(housing_prepared)
forest_mse = mean_squared_error(housing_labels, housing_predictions)
forest_rmse = np.sqrt(forest_mse)
forest_rmse

# %%
from sklearn.model_selection import cross_val_score

forest_scores = cross_val_score(forest_reg, housing_prepared, housing_labels,
                                scoring="neg_mean_squared_error", cv=10)
forest_rmse_scores = np.sqrt(-forest_scores)
display_scores(forest_rmse_scores)

# %% [markdown]
# ## Fine-tune the model

# %%
# to grid search instead of fiddling with hyperparameters manually to find great combinations
from sklearn.model_selection import GridSearchCV

param_grid = [
    # try 12 (3×4) combinations of hyperparameters
    {'n_estimators': [3, 10, 30], 'max_features': [2, 4, 6, 8]},
    # then try 6 (2×3) combinations with bootstrap set as False
    {'bootstrap': [False], 'n_estimators': [3, 10], 'max_features': [2, 3, 4]},
  ]

forest_reg = RandomForestRegressor(random_state=42)
# train across 5 folds, that's a total of (12+6)*5=90 rounds of training 
grid_search = GridSearchCV(forest_reg, param_grid, cv=5,
                           scoring='neg_mean_squared_error',
                           return_train_score=True)
grid_search.fit(housing_prepared, housing_labels)

# %%
# the best hyperparameter combination found:
grid_search.best_params_

# %%
# get best estimator directly
grid_search.best_estimator_

# %%
# look at the relative importance of each attribute for making accurate predictions
feature_importances = grid_search.best_estimator_.feature_importances_

extra_attribs = ["rooms_per_hhold", "pop_per_hhold", "bedrooms_per_room"]
#cat_encoder = cat_pipeline.named_steps["cat_encoder"] # old solution
cat_encoder = full_pipeline.named_transformers_["cat"]
cat_one_hot_attribs = list(cat_encoder.categories_[0])
attributes = num_attribs + extra_attribs + cat_one_hot_attribs
sorted(zip(feature_importances, attributes), reverse=True)

# %% [markdown]
# ## Evaluate the model on the test set

# %%
final_model = grid_search.best_estimator_

X_test = strat_test_set.drop("median_house_value", axis=1)
y_test = strat_test_set["median_house_value"].copy()

X_test_prepared = full_pipeline.transform(X_test)
final_predictions = final_model.predict(X_test_prepared)

final_mse = mean_squared_error(y_test, final_predictions)
final_rmse = np.sqrt(final_mse)
final_rmse

# %%
# compute a 95% confidence interval for the test RMSE
from scipy import stats

confidence = 0.95
squared_errors = (final_predictions - y_test) ** 2
np.sqrt(stats.t.interval(confidence, len(squared_errors) - 1,
                         loc=squared_errors.mean(),
                         scale=stats.sem(squared_errors)))


