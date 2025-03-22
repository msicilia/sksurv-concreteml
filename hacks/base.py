from sklearn.tree import DecisionTreeRegressor
from sksurv.tree import SurvivalTree

def get_params_patched(cls):
     return {"max_depth": cls.max_depth, "max_features": cls.max_features}

def sksurv_model_hack(model):
   """Hack the sksurv model to be compatible with concrete-ml."""
   match model.__class__.__name__:
        case "SurvivalTree":
             # SurvivalTree in disguise as sklearn DecisionTreeRegressor.
             model.__class__ = DecisionTreeRegressor
             # Monkey patch get_params to return the parameters expected by concrete-ml.
             SurvivalTree.get_params = get_params_patched
             # Set the default model parameters expected. 
             # https://github.com/zama-ai/concrete-ml/blob/release/1.8.x/docs/references/api/concrete.ml.sklearn.tree.md#class-decisiontreeregressor
             model.ccp_alpha = 0.0
             model.criterion = "squared_error"
             model.min_impurity_decrease = 0.0
             model.monotonic_cst = None
        case _:
             # TODO: Add other sksurv models.
             pass
   return model