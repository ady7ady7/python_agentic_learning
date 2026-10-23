import mlflow
mlflow.set_tracking_uri('sqlite:///mlflow.db')
mlflow.set_experiment('xauusd_volatility_windows')



with mlflow.start_run(run_name='day2_london_open_to_overlap'):
    mlflow.log_param('window_pair', 'london_open_to_overlap')
    mlflow.log_param('gap_hours', 3)
    mlflow.log_param('max_depth', 4)
    mlflow.log_param('min_samples_leaf', 10)
    mlflow.log_metric('baseline_mae', 0.478)
    mlflow.log_metric('test_mae', 0.364)
    mlflow.log_metric('test_r2', 0.363)
    mlflow.log_metric('train_mae', 0.268)
    mlflow.log_metric('train_r2', 0.645)
    
    
with mlflow.start_run(run_name='day3_premarket_to_overlap1h'):
    mlflow.log_param('window_pair', 'premarket_to_overlap1h')
    mlflow.log_param('gap_hours', 1)
    mlflow.log_param('max_depth', 5)
    mlflow.log_param('min_samples_leaf', 30)
    mlflow.log_metric('baseline_mae', 0.478)
    mlflow.log_metric('test_mae', 0.425)
    mlflow.log_metric('test_r2', 0.183)
    mlflow.log_metric('train_mae', 0.329)
    mlflow.log_metric('train_r2', 0.59)
    
    
    

with mlflow.start_run(run_name='day4_overlap15min_to_resthour'):
    mlflow.log_param('window_pair', 'overlap15min_to_resthour')
    mlflow.log_param('data_granularity', 'M5')
    mlflow.log_param('gap_hours', 0)
    mlflow.log_param('max_depth', 3)
    mlflow.log_param('min_samples_leaf', 30)
    mlflow.log_metric('baseline_mae', 0.493)
    mlflow.log_metric('test_mae', 0.351)
    mlflow.log_metric('test_r2', 0.488)
    mlflow.log_metric('train_mae', 0.240)
    mlflow.log_metric('train_r2', 0.755)
    

best_params = {
    'min_samples_leaf': 5,
    'max_depth': 6
}

mlflow.log_params(best_params)
