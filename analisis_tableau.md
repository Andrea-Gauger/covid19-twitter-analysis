# 🧪 COVID Twitter Analysis

**Análisis avanzado de conversaciones sobre el COVID-19 en Twitter**  
Este proyecto tiene como objetivo explorar, visualizar y contar la historia de cómo se desarrolló la conversación global sobre el COVID-19 a través de la plataforma Twitter, utilizando Tableau como herramienta principal de análisis.

---

## 📦 Dataset

Variables incluidas:

- `tweet_id`, `tweet_url`, `tweet_content`, `tweet_type`, `client`
- `retweets_received`, `likes_received`, `tweet_language`
- `user_id`, `name`, `screen_name`, `user_bio`
- `verified_or_non_verified`, `profile_url`, `protected_or_non_protected`
- `user_followers`, `user_following`, `hashtag`, `mention`
- `account_creation_date`, `tweet_posted_hour`, `tweet_posted_date`, `tweet_country`

---

## 🎯 Objetivos del análisis

- Comprender cómo, cuándo y desde dónde se habló del COVID-19 en Twitter prepandemia
- Identificar los perfiles de usuarios más activos o influyentes
- Analizar los temas y hashtags más relevantes
- Observar el engagement y comportamiento de publicación
- Crear dashboards interactivos y visuales en Tableau que permitan explorar los datos

---

## 📊 Dashboards en Tableau

### 1. 📍 Overview (General)
**Objetivo**: Presentar una visión global del dataset.  
**Incluye**:
- Número total de tweets
- Rango de fechas
- Países representados
- Idiomas identificados
- % de cuentas verificadas y protegidas

---

### 2. ⏱️ Actividad Temporal
**Objetivo**: Detectar patrones de publicación y picos de actividad.  
**Incluye**:
- Tweets por fecha y hora
- Likes y retweets a lo largo del tiempo
- Evolución de hashtags

---

### 3. 🌍 Distribución Geográfica
**Objetivo**: Visualizar la conversación por país.  
**Incluye**:
- Mapa por `tweet_country`
- Ranking de países más activos
- Comparación de engagement entre países

---

### 4. 🧑‍💻 Perfil de Usuario
**Objetivo**: Analizar el tipo de usuarios que generaron los tweets.  
**Incluye**:
- Cuentas verificadas vs. no verificadas
- Distribución de seguidores y seguidos
- Cuentas más activas e influyentes
- Wordcloud de biografías

---

### 5. 💬 Contenido y Engagement
**Objetivo**: Analizar el tipo de contenido publicado y su impacto.  
**Incluye**:
- Tipo de tweet (original, reply, retweet)
- Cliente usado (Twitter Web, iPhone, Android…)
- Engagement por tipo de tweet
- Tweets más virales

---

### 6. #️⃣ Hashtags y Menciones
**Objetivo**: Identificar los temas más recurrentes.  
**Incluye**:
- Hashtags más frecuentes
- Hashtags por país o idioma
- Cuentas más mencionadas

---

### 7. 🗂️ Antigüedad de Cuentas
**Objetivo**: Ver relación entre la fecha de creación de cuentas y su actividad.  
**Incluye**:
- Distribución por `account_creation_date`
- Engagement por antigüedad
- Comparación entre cuentas nuevas y antiguas

---

## 🧵 Narrativa del Proyecto

> "Con este análisis busqué entender cómo reaccionó el mundo en Twitter ante la crisis del COVID. A través de más de X mil tweets, identifiqué patrones de comportamiento, momentos de mayor conversación, perfiles de usuario influyentes, y temas clave que marcaron el discurso público en plena pandemia. El análisis se construyó en Tableau, priorizando el contexto, la transparencia y el storytelling visual."

---

## 🛠 Herramientas utilizadas

- Python (limpieza y preprocesado de datos)
- Tableau (visualización de datos)
- Pandas, NumPy, Regex
- Jupyter Notebook
- Git y GitHub

---

## 📁 Estructura del repositorio

