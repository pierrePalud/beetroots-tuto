
from beetroots.simulations.astro import data_validation
from beetroots.simulations.astro.real_data.real_data_nn import \
    SimulationRealDataNN

if __name__ == "__main__":
    yaml_file, path_data, path_models, path_outputs = SimulationRealDataNN.parse_args()

    params = SimulationRealDataNN.load_params(path_data, yaml_file)

    SimulationRealDataNN.check_input_params_file(
        params,
        data_validation.schema,
    )

    simulation = SimulationRealDataNN(
        **params["simu_init"],
        yaml_file=yaml_file,
        path_data=path_data,
        path_outputs=path_outputs,
        path_models=path_models,
        forward_model_fixed_params=params["forward_model"]["fixed_params"],
    )

    simulation.main(
        params=params,
        path_data_cloud=path_data,
        # point_challenger=point_challenger,
    )
