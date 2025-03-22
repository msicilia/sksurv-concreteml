## sksurv-concreteml

This is an attempt to use survival models in the [scikit-survival](https://github.com/sebp/scikit-survival) library in combination with post-quantization of ML models used in the [concrete-ml](https://github.com/zama-ai/concrete-ml) library. 

This allows survival models to be used under FHE, for privacy preserving inference.

### Idea
The basic assumptions are the following:
- `scikit-survival` is `scikit-learn`-API compatible. 
- Survival models are a particular kind of regressor, so they could be treated as regressors of similar kind that are available in `concrete-ml`.
- 

### Current implementation

The current implementation is just a "hack" of the current APIs of `concrete-ml` and not a proper implementation. This is just done to check the feasibility of the approach. 