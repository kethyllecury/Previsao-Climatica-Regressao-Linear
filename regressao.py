import pandas as pd
import matplotlib.pyplot as plt
from mongo import BancoMongo
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

banco = BancoMongo()
db = banco.get_database()

usuarios = db['orders'] 
resultado = usuarios.find() 

def normalize_json(resultado):
    resultado = pd.json_normalize(resultado, sep='_')  
    return resultado

df = pd.DataFrame(list(resultado))  

df_normalized = pd.concat([normalize_json(doc) for doc in df.to_dict(orient='records')], ignore_index=True)

print(df_normalized.columns)

df_teste = df_normalized[['main_humidity', 'main_temp', 'main_pressure', 'main_feels_like',
                          'main_temp_min', 'main_temp_max', 'main_sea_level', 'main_grnd_level',
                          'visibility']]  

X = df_teste[['main_pressure', 'main_humidity']]
y = df_teste['main_temp'] 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Linear Regression - MSE: {mse:.4f}, R²: {r2:.4f}")

plt.figure(figsize=(8,6))
plt.scatter(y_test, y_pred, color='blue', alpha=0.6)
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', linestyle='--') 
plt.title('Comparação entre Valores Reais e Previsões')
plt.xlabel('Valores Reais')
plt.ylabel('Previsões')
plt.grid(True)
plt.show()