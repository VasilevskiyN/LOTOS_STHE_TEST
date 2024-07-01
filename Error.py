class ErrorCatalog:
    def __init__(self, lang):
        self.lang = lang
        self.errors_catalog = {
            'Backend': {
                1000: 'General Backend Error',
                1101: 'Heat Balance Error',
                1201: 'Thermal Power Error'
            },
            'Frontend': {
                2000: 'General Frontend Error',
                2001: 'UI Loading Error',
                2002: 'Visualization Error'
            },
            'ExternalAPI': {
                3000: 'General External API Error',
                3001: 'API Loading Error',
                3002: 'Request Error'
            }
        }

    def get_error_details(self, error_code):
        if error_code in error_descriptions:
            error_description = error_descriptions[error_code]
            error_category = None
            for category, errors in self.errors_catalog.items():
                if error_code in errors:
                    error_category = category
                    break

            if error_category:
                return {
                    'Category': error_category,
                    'Name': error_description.error_name[self.lang],
                    'Description': error_description.error_description[self.lang],
                    'Severity': error_description.error_severity,
                }
            else:
                return "Error Category not found"
        else:
            return "Error Code not found in descriptions"


class ErrorDescription:
    def __init__(self, error_code, error_name, error_description, error_severity):
        self.error_code = error_code
        self.error_name = error_name
        self.error_description = error_description
        self.error_severity = error_severity

error_descriptions = {
    1201: ErrorDescription(
        1201,
        {
            'en': 'Missing Required Parameters',
            'ru': 'Отсутствуют обязательные параметры',
            'es': 'Faltan parámetros requeridos',
            'fr': 'Paramètres requis manquants',
            'de': 'Fehlende erforderliche Parameter',
            'it': 'Parametri richiesti mancanti',
            'pt': 'Parâmetros obrigatórios em falta',
            'nl': 'Ontbrekende vereiste parameters',
            'ja': '必要なパラメータが欠落しています',
            'zh': '缺少必需参数'
        },
        {
            'en': 'The request is missing required parameters. Please check and provide all necessary parameters.',
            'ru': 'Запрос не содержит обязательных параметров. Пожалуйста, проверьте и предоставьте все необходимые параметры.',
            'es': 'La solicitud está faltando parámetros requeridos. Por favor, verifique y proporcione todos los parámetros necesarios.',
            'fr': 'La requête manque de paramètres requis. Veuillez vérifier et fournir tous les paramètres nécessaires.',
            'de': 'Die Anfrage enthält fehlende erforderliche Parameter. Bitte überprüfen und alle notwendigen Parameter angeben.',
            'it': 'La richiesta manca di parametri richiesti. Si prega di controllare e fornire tutti i parametri necessari.',
            'pt': 'O pedido está faltando parâmetros obrigatórios. Por favor, verifique e forneça todos os parâmetros necessários.',
            'nl': 'Het verzoek mist vereiste parameters. Controleer en verstrek alle noodzakelijke parameters.',
            'ja': 'リクエストに必要なパラメータが欠落しています。すべての必要なパラメータを確認して提供してください。',
            'zh': '请求缺少必需参数。请检查并提供所有必要参数。'
        },
        'Critical'
    )
}

result_from_api = {
    'errorCode': 1201,
    'errorDetails': 'G',
    'errorDebug': 'app_rev2.py:thermal_power',
}

# Create an instance of the ErrorCatalog class
error_catalog = ErrorCatalog('en')
# Get error information based on the error code
error_info = error_catalog.get_error_details(result_from_api['errorCode'])
# Display error information
print(f"Получена ошибка:\n{result_from_api}")
print(f"Расшифровка ошибка:\n{error_info}")