from utils.setup_driver import setup_driver
from utils.fetch_game_data_cached import fetch_game_data_cached
from utils.create_dataframe import create_dataframe


def main(summoner_name: str, region: str) -> None:
    with setup_driver() as driver:
        game_data =  fetch_game_data_cached(driver, summoner_name, region)
        df = create_dataframe(game_data)

        if df is not None:
            df.to_csv(f"{summoner_name}_{region}_stats.csv")
        else:
            print("Error: could not create DataFrame")

if __name__ == "__main__":
    summoner_name: str = "itzpipeqlo"
    region: str = "las"
    main(summoner_name, region)
