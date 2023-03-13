import optuna

from objective import objective_factory
from optuna.samplers import RandomSampler


print("mysql")
study1 = optuna.create_study(study_name="test", storage="mysql+pymysql://root:root@mysql:3306/optuna", sampler=RandomSampler())
study1.optimize(objective_factory(allow_inf=False, allow_nan=False), n_trials=10)
print("postgresql")
study2 = optuna.create_study(study_name="test", storage="postgresql+psycopg2://root:root@postgresql/optuna", sampler=RandomSampler())
study2.optimize(objective_factory(allow_inf=True, allow_nan=False), n_trials=10)
print("sqlite")
study3 = optuna.create_study(study_name="test", storage="sqlite:///data/sample.db", sampler=RandomSampler())
study3.optimize(objective_factory(allow_inf=True, allow_nan=False), n_trials=10)

print("done")
