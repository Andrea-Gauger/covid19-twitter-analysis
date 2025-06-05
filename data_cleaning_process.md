# 📊 Análisis Exploratorio de Tweets sobre Covid-19

Este proyecto incluye un análisis exploratorio de datos (EDA) de un conjunto de más de 60.000 tweets. El objetivo es limpiar, transformar y preparar los datos para un análisis posterior y su visualización en Tableau.

Se han llevado a cabo tareas como detección de nulos, limpieza de texto, transformación de fechas, identificación de hashtags y menciones, y creación de nuevas columnas. El archivo final está preparado para visualización.

---

## 🇪🇸 Español

### 1. EDA

Primer análisis exploratorio:

- 60.160 filas y 22 columnas  
- No hay filas duplicadas  
- Las columnas se pueden renombrar por buenas prácticas usando el guión bajo  

**Las columnas son las siguientes:**

0. Tweet Id (object)  
1. Tweet URL (object)  
   - Útil para poder acceder al tweet real  
2. Tweet Posted Time (UTC) (object)  
   - Crear una nueva columna con solo la fecha  
   - Crear una nueva columna con solo la hora  
3. Tweet Content (object)  
   - Acceder a lo que está escrito después del # y del @  
4. Tweet Type (object)  
   - ReTweet: 45.291  
   - Tweet: 13.734  
   - Reply: 1.135  
5. Client (object)  
   - Tiene muchos valores únicos, se puede realizar un TOP5  
6. Retweets Received (int64)  
7. Likes Received (int64)  
8. Tweet Location (object)  
   - No se ha rellenado de forma consistente, buscar un modo de limpiar sin perder demasiados datos  
   - Tiene un número considerable de nulos  
9. Lat (float64) → casi todo Nulos → eliminar  
10. Long (float64) → casi todo Nulos → eliminar  
11. Tweet Language (object)  
   - No está normalizada, contiene un número considerable de nulos  
12. User Id (object)  
13. Name (object) → un valor Nulo → corregir como 'Unk'  
14. Screen Name (object)  
15. User Bio (object)  
16. Verified or Non-Verified (object)  
   - Non-Verified: 54.236  
   - Verified: 5.924  
17. Profile URL (object)  
18. Protected or Non-protected (object) → todos son Non-protected  
19. User Followers (int64)  
20. User Following (int64)  
21. User Account Creation Date (object) → crear columna solo con año  

---

### 2. Nulos

- Elimino las columnas 'Lat' y 'Long', casi 100% de Nulos  
- 1 Nulo en 'Name' → se convierte en 'Unk'  
- 'User Bio' tiene un 17% de Nulos → se convierte en 'Unk'  

**Pendientes: 'Tweet Location' (32%) y 'Tweet Language' (2%)**

---

### 3. Limpieza

- **Tweet Content**  
  - Extraigo Hashtags (#) y Menciones (@) en nuevas columnas  

- **User Account Creation Date**  
  - Nueva columna con solo el año → `account_creation_year`  

- **Tweet Posted Time (UTC)**  
  - Nueva columna con solo la fecha  
  - Nueva columna con solo la hora  

- **Tweet Location**  
  - Relleno NaNs con 'Unk'  
  - Limpieza con mapeo de países y abreviaturas  
  - Nueva columna: `tweet_country`  
  - Elimino 'Tweet Location' y 'tweet_location_clean'  

- **Tweet Language**  
  - Las ocurrencias menores a 10 → 'Other'  
  - NaNs → 'Unk'  
  - Reemplazo 'in' por 'Indonesia'  

---

### 4. Duplicados

- No hay filas duplicadas  
- 'User Id': 16.863 duplicados  
- 'Name': 18.619 duplicados  
  - Son distintos usuarios con el mismo nombre  

---

### 5. Guardar CSV

- Creación de un nuevo `.csv` limpio listo para cargar en Tableau  

---

### 🇬🇧 English

# 📊 Exploratory Data Analysis of Tweets on COVID-19

This project includes an exploratory data analysis (EDA) of a dataset containing over 60,000 tweets. The goal is to clean, transform, and prepare the data for further analysis and visualization in Tableau.  

Tasks performed include null value handling, text cleaning, date and time transformation, hashtag and mention extraction, and the creation of new columns. The final file is ready for visualization.

---

### 1. EDA

Initial exploratory analysis:

- 60,160 rows and 22 columns  
- No duplicate rows  
- Columns renamed using underscores for best practices  

**The columns are as follows:**

0. Tweet Id (object)  
1. Tweet URL (object)  
   - Useful to access the original tweet  
2. Tweet Posted Time (UTC) (object)  
   - Create new column with date only  
   - Create new column with time only  
3. Tweet Content (object)  
   - Extract text after # and @  
4. Tweet Type (object)  
   - ReTweet: 45,291  
   - Tweet: 13,734  
   - Reply: 1,135  
5. Client (object)  
   - Many unique values, could extract TOP5  
6. Retweets Received (int64)  
7. Likes Received (int64)  
8. Tweet Location (object)  
   - Inconsistent values, try to clean without losing too much  
   - High number of nulls  
9. Lat (float64) → mostly nulls → drop  
10. Long (float64) → mostly nulls → drop  
11. Tweet Language (object) → inconsistent, some nulls  
12. User Id (object)  
13. Name (object) → 1 null → set as 'Unk'  
14. Screen Name (object)  
15. User Bio (object)  
16. Verified or Non-Verified (object)  
   - Non-Verified: 54,236  
   - Verified: 5,924  
17. Profile URL (object)  
18. Protected or Non-protected (object) → all are Non-protected  
19. User Followers (int64)  
20. User Following (int64)  
21. User Account Creation Date (object) → extract year only  

---

### 2. Nulls

- Dropped 'Lat' and 'Long' due to nearly 100% nulls  
- 1 null in 'Name' → replaced with 'Unk'  
- 17% nulls in 'User Bio' → replaced with 'Unk'  

**Remaining: 'Tweet Location' (32%) and 'Tweet Language' (2%)**

---

### 3. Cleaning

- **Tweet Content**  
  - New columns for Hashtags (#) and Mentions (@)  

- **User Account Creation Date**  
  - Extracted `account_creation_year`  

- **Tweet Posted Time (UTC)**  
  - New columns for date and time  

- **Tweet Location**  
  - Fill NaNs with 'Unk'  
  - Map and clean using country list  
  - Final column: `tweet_country`  
  - Dropped original 'Tweet Location' and 'tweet_location_clean'  

- **Tweet Language**  
  - Values with <10 occurrences → 'Other'  
  - Nulls → 'Unk'  
  - Replaced 'in' with 'Indonesia'  

---

### 4. Duplicates

- No exact row duplicates  
- 'User Id': 16,863 duplicates  
- 'Name': 18,619 duplicates  
  - Different users share the same name  

---

### 5. Save CSV

- Cleaned `.csv` file ready for Tableau visualization  

---

### 🇮🇹 Italiano

# 📊 Analisi Esplorativa dei Tweet su LA COVID-19

Questo progetto comprende un’analisi esplorativa dei dati (EDA) di un dataset con oltre 60.000 tweet. L’obiettivo è pulire, trasformare e preparare i dati per analisi successive e visualizzazione in Tableau.  

Le attività svolte includono la gestione dei valori nulli, la pulizia del testo, la trasformazione di date e orari, l’estrazione di hashtag e menzioni, e la creazione di nuove colonne. Il file finale è pronto per essere visualizzato.

---

### 1. EDA

Prima analisi esplorativa:

- 60.160 righe e 22 colonne  
- Nessuna riga duplicata  
- Rinominate le colonne con underscore per seguire le best practices  

**Le colonne sono:**

0. Tweet Id (object)  
1. Tweet URL (object)  
   - Utile per accedere al tweet reale  
2. Tweet Posted Time (UTC) (object)  
   - Nuova colonna con solo la data  
   - Nuova colonna con solo l'ora  
3. Tweet Content (object)  
   - Estrarre testo dopo # e @  
4. Tweet Type (object)  
   - ReTweet: 45.291  
   - Tweet: 13.734  
   - Reply: 1.135  
5. Client (object)  
   - Molti valori unici, possibile fare un TOP5  
6. Retweets Received (int64)  
7. Likes Received (int64)  
8. Tweet Location (object)  
   - Valori incoerenti, da pulire senza perdere troppi dati  
   - Contiene molti nulli  
9. Lat (float64) → quasi tutto nullo → eliminare  
10. Long (float64) → quasi tutto nullo → eliminare  
11. Tweet Language (object) → valori incoerenti, anche alcuni nulli  
12. User Id (object)  
13. Name (object) → 1 nullo → sostituire con 'Unk'  
14. Screen Name (object)  
15. User Bio (object)  
16. Verified or Non-Verified (object)  
   - Non-Verified: 54.236  
   - Verified: 5.924  
17. Profile URL (object)  
18. Protected or Non-protected (object) → tutti sono Non-protected  
19. User Followers (int64)  
20. User Following (int64)  
21. User Account Creation Date (object) → estrarre solo l’anno  

---

### 2. Valori Nulli

- Eliminato 'Lat' e 'Long' (quasi 100% nulli)  
- 1 valore nullo in 'Name' → sostituito con 'Unk'  
- 'User Bio' 17% nulli → sostituito con 'Unk'  

**Restano da trattare: 'Tweet Location' (32%) e 'Tweet Language' (2%)**

---

### 3. Pulizia

- **Tweet Content**  
  - Nuove colonne per Hashtag (#) e Menzioni (@)  

- **User Account Creation Date**  
  - Estratto `account_creation_year`  

- **Tweet Posted Time (UTC)**  
  - Nuove colonne per data e ora  

- **Tweet Location**  
  - Riempiti i NaN con 'Unk'  
  - Mappati e puliti con elenco paesi  
  - Colonna finale: `tweet_country`  
  - Eliminate 'Tweet Location' e 'tweet_location_clean'  

- **Tweet Language**  
  - Valori con meno di 10 occorrenze → 'Other'  
  - Nulli → 'Unk'  
  - Sostituito 'in' con Indonesia  

---

### 4. Duplicati

- Nessuna riga duplicata  
- 'User Id': 16.863 duplicati  
- 'Name': 18.619 duplicati  
  - Utenti diversi con lo stesso nome  

---

### 5. Salvataggio CSV

- File `.csv` pulito pronto per essere caricato in Tableau  
