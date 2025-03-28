from qgis.core import QgsProcessingProvider
from qgis.PyQt.QtGui import QIcon

from .main import BasicProcessingTool  # Import your custom algorithm class


class CustomProcessingProvider(QgsProcessingProvider):
    def loadAlgorithms(self):
        # Add your geoprocessing algorithm to the provider
        self.addAlgorithm(BasicProcessingTool())

    def id(self):
        return "custom_provider"

    def name(self):
        return "Custom Provider"

    def icon(self):
        # Provide the path to the icon using the resource system
        return QIcon(":/BasicPlugin/icon.png")
