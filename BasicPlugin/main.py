from qgis.core import (QgsFeature, QgsFeatureRequest, QgsFeatureSink, QgsField,
                       QgsGeometry, QgsProcessing, QgsProcessingAlgorithm,
                       QgsProcessingException, QgsProcessingOutputVectorLayer,
                       QgsProcessingParameterDistance,
                       QgsProcessingParameterFeatureSink,
                       QgsProcessingParameterFeatureSource,
                       QgsProcessingParameterVectorLayer, QgsSpatialIndex,
                       QgsWkbTypes)
from qgis.utils import iface


class BasicProcessingTool(QgsProcessingAlgorithm):
    INPUT = "INPUT"
    OUTPUT = "OUTPUT"

    def initAlgorithm(self, config=None):
        # Define input and output parameters
        self.addParameter(
            QgsProcessingParameterFeatureSource(self.INPUT, "Input Layer")
        )
        self.addParameter(
            QgsProcessingParameterFeatureSink(self.OUTPUT, "Output Layer")
        )

    def processAlgorithm(self, parameters, context, feedback):
        # Get input layer
        input_layer = self.parameterAsSource(parameters, self.INPUT, context)
        if input_layer is None:
            raise QgsProcessingException("Invalid input layer")

        # Set up output
        (sink, sink_id) = self.parameterAsSink(
            parameters,
            self.OUTPUT,
            context,
            input_layer.fields(),
            input_layer.wkbType(),
            input_layer.sourceCrs(),
        )

        # Process each feature
        for feature in input_layer.getFeatures():
            # Add feature to output
            sink.addFeature(feature, QgsFeatureSink.FastInsert)

        return {self.OUTPUT: sink_id}

    def name(self):
        return "basicprocessingtool"

    def displayName(self):
        return "Basic Processing Tool"

    def group(self):
        return "Custom Scripts"

    def groupId(self):
        return "customscripts"

    def createInstance(self):
        return BasicProcessingTool()
