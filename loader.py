from dependency_injector import providers, containers
from route.AiRoute import AiRoute
from service.AiService import AiService
from model.CnnModel import CnnModel


class Model(containers.DeclarativeContainer):
    cnnModel = providers.Singleton(CnnModel)

class Service(containers.DeclarativeContainer):
    aiService = providers.Singleton(AiService, cnnModel=Model.cnnModel)

class Route(containers.DeclarativeContainer):
    aiRoute = providers.Singleton(AiRoute, aiService=Service.aiService)
    