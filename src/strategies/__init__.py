from strategies import first_only, one_by_one
import config

if config.processing_strategy == "FIRST_ONLY":
    STRATEGY = first_only.FirstOnlyStrategy()
elif config.processing_strategy == "ONE_BY_ONE":
    STRATEGY = one_by_one.OneByOneStrategy()
else:
    raise Exception("Bad strategy type")
