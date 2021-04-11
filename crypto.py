from PyQt5.QtCore import *
import traceback
import requests


# CryptoCompare.com API Key
CRYPTOCOMPARE_API_KEY = 'a4a717e695ceee571062b05cf367b51317d57779b6fc53234abd5ce14659e81f'

# The crypto currencies to retrieve data about.
AVAILABLE_CRYPTO_CURRENCIES = ['BTC', 'ETH', 'LTC', 'EOS', 'XRP', 'BCH' ]

# Number of historic timepoints to plot (days).
NUMBER_OF_TIMEPOINTS = 150

class WorkerSignals(QObject):
    """
    Defines the signals available from a running worker thread.
    """
    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    progress = pyqtSignal(int)
    data = pyqtSignal(dict, list)
    cancel = pyqtSignal()

class UpdateWorker(QRunnable):
    """
    Worker thread for updating currency.
    """
    signals = WorkerSignals()

    def __init__(self, base_currency):
        super(UpdateWorker, self).__init__()
        self.is_interrupted = False
        self.base_currency = base_currency
        self.signals.cancel.connect(self.cancel)

    @pyqtSlot()
    def run(self):
        auth_header = {
            'Apikey': CRYPTOCOMPARE_API_KEY
        }
        try:
            rates = {}
            for n, crypto in enumerate(AVAILABLE_CRYPTO_CURRENCIES, 1):
                url = 'https://min-api.cryptocompare.com/data/histoday?fsym={fsym}&tsym={tsym}&limit={limit}'
                r = requests.get(
                    url.format(**{
                        'fsym': crypto,
                        'tsym': self.base_currency,
                        'limit': NUMBER_OF_TIMEPOINTS-1,
                        'extraParams': 'www.learnpyqt.com',
                        'format': 'json',
                    }),
                    headers=auth_header,
                )
                r.raise_for_status()
                rates[crypto] = r.json().get('Data')

                self.signals.progress.emit(int(100 * n / len(AVAILABLE_CRYPTO_CURRENCIES)))

                if self.is_interrupted:
                    # Stop without emitting finish signals.
                    return

            url = 'https://min-api.cryptocompare.com/data/exchange/histoday?tsym={tsym}&limit={limit}'
            r = requests.get(
                url.format(**{
                    'tsym': self.base_currency,
                    'limit': NUMBER_OF_TIMEPOINTS-1,
                    'extraParams': 'www.learnpyqt.com',
                    'format': 'json',
                }),
                headers=auth_header,
            )
            r.raise_for_status()
            volume = [d['volume'] for d in r.json().get('Data')]

        except Exception as e:
            self.signals.error.emit((e, traceback.format_exc()))
            return

        self.signals.data.emit(rates, volume)
        self.signals.finished.emit()

    def cancel(self):
        self.is_interrupted = True

