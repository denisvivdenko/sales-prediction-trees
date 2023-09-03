import argparse

from src.utils.configuration import load_params


if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument("--config", dest="config", required=True, type=str)
    args = argparser.parse_args()
    config_path = args.config

    params = load_params(config_path)
    print(params)