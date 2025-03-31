import xgboost as xgb
from xgboost import XGBClassifier
from sklearn.metrics import roc_auc_score, accuracy_score
from ember import read_vectorized_features


def train_model(data_dir, config=None):
    X_train, y_train, X_test, y_test = read_vectorized_features(data_dir)

    # ✅ Filter out unknown labels (-1)
    mask_train = y_train != -1
    mask_test = y_test != -1

    X_train = X_train[mask_train]
    y_train = y_train[mask_train]
    X_test = X_test[mask_test]
    y_test = y_test[mask_test]

    model = XGBClassifier(
        tree_method="gpu_hist",
        gpu_id=0,
        scale_pos_weight=7.0,
        n_estimators=100,
        learning_rate=0.1,
        max_depth=6,
        subsample=0.8,
        colsample_bytree=0.8,
        use_label_encoder=False,
        eval_metric="auc",
        random_state=42
    )

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    y_proba = model.predict_proba(X_test)[:, 1]

    auc = roc_auc_score(y_test, y_proba)
    acc = accuracy_score(y_test, y_pred)

    return model, {"auc": auc, "accuracy": acc}
