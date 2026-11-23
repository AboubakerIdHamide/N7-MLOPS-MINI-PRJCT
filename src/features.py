from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer, StandardScaler


def _clip(X):
    """Limit standardized values to [-3, 3] to reduce the effect of outliers."""
    return X.clip(-3, 3)


def build_numeric_preprocess():
    """Impute missing values, standardize features, then clip to [-3, 3]."""
    return Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler()),
            ("clip", FunctionTransformer(_clip)),
        ]
    )
