from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DateRange,
    Dimension,
    Metric,
    RunReportRequest,
)
from google.oauth2 import service_account

# Caminho para o arquivo de credenciais JSON
credentials_path = "security/analytics-clientco-82d3234933c0.json"

# Autenticação usando Service Account
credentials = service_account.Credentials.from_service_account_file(
    credentials_path,
    scopes=["https://www.googleapis.com/auth/analytics.readonly"],
)

# Inicializa o cliente da API
client = BetaAnalyticsDataClient(credentials=credentials)

# ID da propriedade do GA4 (substitua pelo seu ID)
property_id = "376938583"

# Cria a requisição para o relatório
request = RunReportRequest(
    property=f"properties/{property_id}",
    dimensions=[Dimension(name="date")],
    metrics=[Metric(name="activeUsers")],
    date_ranges=[DateRange(start_date="2025-02-24", end_date="2025-02-24")],
)

# Executa a requisição e obtém a resposta
response = client.run_report(request)

# Exibe os resultados
print("Relatório de Usuários Ativos:")
for row in response.rows:
    print(f"Data: {row.dimension_values[0].value}, Usuários Ativos: {row.metric_values[0].value}")