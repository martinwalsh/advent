import Config

config :advent,
  year: DateTime.utc_now().year - if(DateTime.utc_now().month == 12, do: 1, else: 0)

config :logger, level: if(System.get_env("DEBUG") != "", do: :debug, else: :info)
