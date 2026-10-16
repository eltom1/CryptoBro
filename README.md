# CrypToBro

<img alt="Python" src="https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python&logoColor=white">   <img alt="Telegram" src="https://img.shields.io/badge/Telegram-26A5E4?style=flat-square&logo=telegram&logoColor=white">

CrypToBro es un asistente financiero de Telegram. Su objetivo es facilitar la recolección de información sobre distintos mercados, proporcionando alertas y análisis de activos en tiempo real para optimizar la toma de decisiones de inversión, monitoreando múltiples mercados, tanto locales como internacionales.

## Mapeo de ecosistemas de inversión

- **Criptomonedas** 
  - **Monitoreo:** = Seguimiento de precios en tiempo real vía WebSockets (Binance/CCXT).
  - **Análisis:** = Detección de rupturas de precio y seguimiento de monedas estables (USDT, USDC).
  - **Objetivo:** = Alertar sobre caídas abruptas (oportunidades de compra) o alzas parabólicas.

- **Empresas(Bolsa Global)**
  - **Monitoreo:** = Acciones de empresas líderes (S&P 500, NASDAQ) a través de Yahoo Finance.
  - **Análisis:** =  Seguimiento de empresas tecnológicas, energéticas y de consumo.
  - **Objetivo:** = Analizar el rendimiento de activos como NVDA, TSLA, AAPL y más.

- **Mercado local**
  - **Monitoreo:** = Seguimiento preciso de las diversas cotizaciones del dólar (Blue, Oficial, MEP, CCL) y bonos locales.
  - **Análisis:** = Comparativa de brecha cambiaria y valor real del peso.
  - **Objetivo:** = Optimizar la compra de moneda extranjera y proteger el capital contra la inflación.

- **Inversiones inmobiliarias**
  - **Análisis:** = Mapeo de rentabilidad por m² y seguimiento de índices de precios de propiedades.
  - **Objetivo:** = Evaluar la viabilidad de inversiones en ladrillos comparado con activos líquidos.

- **Fondos comunes de inversión**
  - **Monitoreo:** = Comparativa de rendimientos entre diferentes fondos y gestoras.
  - **Análisis:** =  Evaluación de riesgo vs. retorno.
  - **Objetivo:** = Encontrar la mejor tasa de interés para el dinero en espera (liquidez inmediata).
 

## Roadmap develop
- [x] Conexión básica con Telegram Bot API.
- [x] Implementación de cotizaciones de Dólar local en tiempo real (Blue, Oficial).  -- 15/10/26
- [ ] Integración de precios de Criptomonedas en tiempo real vía API de Binance.
- [ ] Implementación de consulta de Acciones globales y ETFs vía Yahoo Finance.
- [ ] Desarrollo de un sistema de Watchlist para seguimiento de activos personalizados.
- [ ] Sistema de alertas automáticas basadas en porcentaje de cambio brusco (Volatilidad).
- [ ] Implementación de base de datos SQLite para almacenamiento de precios históricos.
- [ ] **Módulo de Análisis Técnico:** Implementación de Bandas de Bollinger, Fibonacci y Ondas de Elliott.
- [ ] **Detector de Patrones:** Reconocimiento automático de velas japonesas y rupturas de precio.
- [ ] **Análisis Fundamental:** Integración de noticias macroeconómicas y monitoreo de Tokenomics.
- [ ] **Medidor de Sentimiento:** Conexión con el Fear & Greed Index y rastreo de movimientos de Ballenas.
- [ ] **Modelado Estadístico:** Implementación de modelos ARIMA para proyecciones de precios.
- [ ] **Asistente de Gestión:** Recomendaciones de estrategias DCA según el ciclo de mercado.
- [ ] Dashboard de seguimiento de cartera personal con cálculo de ganancias/pérdidas.
- [ ] Mapeo de rentabilidad de Inversiones Inmobiliarias y fondos comunes de inversión (FCI).
- [ ] Integración de IA para análisis predictivo y resúmenes de noticias financieras.
- [ ] Automatización de órdenes de compra/venta reales mediante API Keys.


